from contextlib import asynccontextmanager
from typing import Union, List

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from lib import Loader, CacheManager
from models import FeatureCollection, Feature, MapParams, Comune, ComuneBase, ComuneRequest
from services import MapService

loader = Loader()
cache = CacheManager()
map_service = MapService(cache)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await cache.store("all_comuni", loader.load_mini())
    await cache.store("all_comuni_full", loader.load_all())
    await cache.store("maps", loader.load_map())
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def home():
    return RedirectResponse(url="/docs")


@app.get("/comuni", tags=["Comuni"], response_model=List[ComuneBase])
async def get_comuni():
    """
    Ritorna l'elenco di tutti i comuni con i campi minimi.
    """
    try:
        data = await cache.read("all_comuni")
        if not data:
            filtered = loader.load_mini()
            await cache.store("all_comuni", filtered)
            data = filtered
        return [ComuneBase(**row) for row in data]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/comuni/{istat}", tags=["Comuni"], response_model=Comune)
async def get_comune(request: ComuneRequest = Depends()):
    """
    Ritorna i dati di un comune specifico a partire dal suo codice ISTAT (es: 082053).
    """
    try:
        data = await cache.read("all_comuni_full")
        if not data:
            full = loader.load_all()
            await cache.store("all_comuni_full", full)
            data = full

        result = next((c for c in data if c.get("pro_com_t") == request.istat), None)
        if not result:
            raise HTTPException(status_code=404, detail="Comune non trovato.")

        return Comune(**result)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/map", response_model=Union[Feature, FeatureCollection], tags=["Mappe"])
async def get_map(params: MapParams = Depends(MapParams)):
    """
    Ritorna i dati geografici dei comuni siciliani,
    - Se il 'comune' è specificato, ritorna una singola Feature.
    - Se la 'provincia' è specificata, ritorna una FeatureCollection.
    """
    try:
        return await map_service.get_map_data(params)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

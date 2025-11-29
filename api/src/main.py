from contextlib import asynccontextmanager
from typing import Union, List

from fastapi import FastAPI, HTTPException, Depends, Path
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from lib import Loader, CacheManager
from models import FeatureCollection, Feature, MapParams, Comune, ComuneBase
from services import MapService

loader = Loader()
cache = CacheManager()
map_service = MapService(cache)


@asynccontextmanager
async def lifespan(app: FastAPI):
    cache.store("all_comuni", loader.load_mini())
    cache.store("all_comuni_full", loader.load_all())
    cache.store("maps", loader.load_map())
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
        data = cache.read("all_comuni")
        return [ComuneBase(**row) for row in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/comuni/{istat}", tags=["Comuni"], response_model=Comune)
async def get_comune(istat: str = Path(..., min_length=6, max_length=6, description="Codice ISTAT del comune")):
    """
    Ritorna i dati di un comune specifico a partire dal suo codice ISTAT (es: 082053).
    """
    try:
        if not istat.isdigit():
            raise HTTPException(status_code=400, detail="Il codice ISTAT non è valido.")

        data = cache.read("all_comuni_full")
        result = next((c for c in data if c.get("pro_com_t") == istat), None)

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

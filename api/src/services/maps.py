from typing import Union

from fastapi import HTTPException

from models import Feature, FeatureCollection, MapParams


class MapService:
    def __init__(self, cache):
        self.cache = cache

    async def get_map_data(self, params: MapParams) -> Union[Feature, FeatureCollection]:
        if not params.comune and not params.provincia:
            raise HTTPException(status_code=422, detail="Devi specificare almeno un comune o una provincia.")

        geojson_data = self.cache.read("maps")
        features = geojson_data.get("features", [])

        if params.comune:
            feature_data = next(
                (feat for feat in features if feat["properties"].get("PRO_COM_T") == params.comune),
                None
            )
            if not feature_data:
                raise HTTPException(status_code=404, detail=f"Comune '{params.comune}' non trovato.")
            return Feature.from_geojson(feature_data)

        filtered_features_data = [
            feat for feat in features
            if str(feat["properties"].get("COD_PROV")) == params.provincia
        ]
        if not filtered_features_data:
            raise HTTPException(status_code=404, detail=f"Nessuna feature trovata per la provincia {params.provincia}.")

        return FeatureCollection.from_geojson(geojson_data, filtered_features_data)

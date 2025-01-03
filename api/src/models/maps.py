from typing import Any, List, Optional

from pydantic import BaseModel, Field


class MapParams(BaseModel):
    comune: Optional[str] = Field(default=None, description="Nome del comune.")
    provincia: Optional[str] = Field(default=None, description="Codice della provincia.")


class Feature(BaseModel):
    type: str
    geometry_type: str
    coordinates: Any
    PRO_COM_T: Optional[str] = None
    COD_PROV: Optional[int] = None

    @classmethod
    def from_geojson(cls, feat: dict) -> 'Feature':
        return cls(
            type=feat.get("type"),
            geometry_type=feat["geometry"].get("type"),
            coordinates=feat["geometry"].get("coordinates"),
            PRO_COM_T=feat["properties"].get("PRO_COM_T"),
            COD_PROV=feat["properties"].get("COD_PROV")
        )


class FeatureCollection(BaseModel):
    type: str
    name: str
    crs_type: str
    crs_name: str
    features: List[Feature]

    @classmethod
    def from_geojson(cls, geojson_data: dict, filtered_features: List[dict]) -> 'FeatureCollection':
        return cls(
            type=geojson_data.get("type", "FeatureCollection"),
            name=geojson_data.get("name", "comuni_siciliani2021"),
            crs_type=geojson_data.get("crs", {}).get("type", "name"),
            crs_name=geojson_data.get("crs", {}).get("properties", {}).get("name", ""),
            features=[Feature.from_geojson(feat) for feat in filtered_features]
        )

    def to_crs(self):
        return {
            "type": self.crs_type,
            "properties": {
                "name": self.crs_name
            }
        }

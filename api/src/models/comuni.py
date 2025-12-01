from typing import Optional

from pydantic import BaseModel, Field, field_validator


class ComuneRequest(BaseModel):
    istat: str = Field(..., min_length=6, max_length=6, description="Codice ISTAT del comune.")

    @field_validator("istat")
    def validate_istat(cls, value: str) -> str:
        if not value.isdigit():
            raise ValueError("Il codice ISTAT non è valido.")
        return value


class ComuneBase(BaseModel):
    pro_com_t: str
    comune: str
    sigla: str
    pop_res_21: Optional[str] = None


class Comune(ComuneBase):
    lat: Optional[str] = None
    long: Optional[str] = None
    den_prov: Optional[str] = None
    den_reg: Optional[str] = None
    cod_reg: Optional[str] = None
    cap: Optional[str] = None
    cf: Optional[str] = None
    pec: Optional[str] = None
    mail: Optional[str] = None
    sito_web: Optional[str] = None
    wikipedia: Optional[str] = None
    stemma: Optional[str] = None
    pop_res_21: Optional[str] = None

from pydantic import BaseModel, Field


class Inference(BaseModel):
    label: str = Field(...)
    confidence: float = Field(..., ge=0.0, le=1.0)

    class Config:
        allow_mutation = False

from dataclasses import dataclass


@dataclass(frozen=True)
class Inference:
    id: str
    confidence: float

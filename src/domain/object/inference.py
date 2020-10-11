from dataclasses import dataclass


@dataclass(frozen=True)
class Inference:
    label: str
    confidence: float

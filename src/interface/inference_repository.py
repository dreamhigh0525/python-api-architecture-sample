from abc import ABCMeta, abstractmethod
from src.domain.inference import Inference


class AbstractInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_inference(self) -> Inference:
        raise NotImplementedError

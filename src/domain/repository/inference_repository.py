from abc import ABCMeta, abstractmethod
from src.domain.object.inference import Inference


class AbstructInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_inference(self, data) -> Inference:
        raise NotImplementedError

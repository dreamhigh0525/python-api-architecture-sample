from abc import ABCMeta, abstractmethod
from src.domain.object.image import Image
from src.domain.object.inference import Inference


class AbstructInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_inference(self, data: Image) -> Inference:
        raise NotImplementedError

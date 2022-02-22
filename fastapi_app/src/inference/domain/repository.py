from abc import ABCMeta, abstractmethod
from .content import Content
from .inference import Inference
from .inference_type import InferenceType


class InferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    async def get_inference(self, type: InferenceType, content: Content) -> Inference:
        raise NotImplementedError
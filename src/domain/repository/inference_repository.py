from abc import ABCMeta, abstractmethod
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.object.inference_type import InferenceType


class AbstructInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_inference(self, type: InferenceType, data: Content) -> Inference:
        raise NotImplementedError

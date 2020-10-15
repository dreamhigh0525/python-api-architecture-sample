from abc import ABCMeta, abstractmethod
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.object.inference_type import InferenceType


class AbstractInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_inference(self, type: InferenceType, content: Content) -> Inference:
        raise NotImplementedError

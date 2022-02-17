from abc import ABCMeta, abstractmethod
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.object.inference_type import InferenceType


class AbstractInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_inference(self, type: InferenceType, content: Content) -> Inference:
        raise NotImplementedError

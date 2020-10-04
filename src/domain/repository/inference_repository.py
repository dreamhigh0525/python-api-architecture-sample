from abc import ABCMeta, abstractmethod
from src.domain.object.content import Content
from src.domain.object.inference import Inference


class AbstructInferenceRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_inference(self, data: Content) -> Inference:
        raise NotImplementedError

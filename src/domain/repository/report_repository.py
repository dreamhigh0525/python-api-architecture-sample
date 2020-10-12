from abc import ABCMeta, abstractmethod
from src.domain.object.content import Content
from src.domain.object.inference import Inference


class AbstructReportRepository(metaclass=ABCMeta):
    @abstractmethod
    def report_inference(self, content: Content, inference: Inference) -> None:
        raise NotImplementedError

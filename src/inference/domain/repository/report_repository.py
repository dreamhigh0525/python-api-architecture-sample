from abc import ABCMeta, abstractmethod
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference


class AbstractReportRepository(metaclass=ABCMeta):
    @abstractmethod
    def report_inference(self, content: Content, inference: Inference) -> None:
        raise NotImplementedError

from abc import ABCMeta, abstractmethod
from src.domain.object.inference import Inference


class AbstructReportRepository(metaclass=ABCMeta):
    @abstractmethod
    def report_inference(self, data: Inference) -> None:
        raise NotImplementedError

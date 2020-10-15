from injector import Injector, Module
from src.domain.repository.inference_repository import AbstractInferenceRepository
from src.domain.repository.report_repository import AbstractReportRepository
from src.infrastructure.repository.inference_repository import InferenceRepository
from src.infrastructure.repository.report_repository import ReportRepository


class InferenceDIModule(Module):
    def configure(self, binder):
        binder.bind(AbstractInferenceRepository, to=InferenceRepository)


class ReportDIModule(Module):
    def configure(self, binder):
        binder.bind(AbstractReportRepository, to=ReportRepository)


injector = Injector([InferenceDIModule(), ReportDIModule()])

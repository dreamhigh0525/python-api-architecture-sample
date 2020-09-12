from injector import Injector, Module
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.domain.repository.report_repository import AbstructReportRepository
from src.infrastructure.repository.inference_repository import InferenceRepository
from src.infrastructure.repository.report_repository import ReportRepository


class InferenceDIModule(Module):
    def configure(self, binder):
        binder.bind(AbstructInferenceRepository, to=InferenceRepository)


class ReportDIModule(Module):
    def configure(self, binder):
        binder.bind(AbstructReportRepository, ReportRepository)


injector = Injector([InferenceDIModule(), ReportDIModule()])

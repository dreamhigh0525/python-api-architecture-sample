from injector import Binder, Injector, Module
from inference.domain.repository.inference_repository import AbstractInferenceRepository
from inference.domain.repository.report_repository import AbstractReportRepository
from inference.infrastructure.repository.inference_repository import InferenceRepository
from inference.infrastructure.repository.report_repository import ReportRepository


class InferenceDIModule(Module):
    def configure(self, binder: Binder):
        binder.bind(AbstractInferenceRepository, to=InferenceRepository)


class ReportDIModule(Module):
    def configure(self, binder: Binder):
        binder.bind(AbstractReportRepository, to=ReportRepository)


injector = Injector([InferenceDIModule(), ReportDIModule()])

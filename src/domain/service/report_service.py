from injector import inject
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.repository.report_repository import AbstructReportRepository


class ReportService():
    report_repository: AbstructReportRepository

    @inject
    def __init__(self, report_repository: AbstructReportRepository):
        self.report_repository = report_repository

    def report_inference(self, content: Content, inference: Inference) -> None:
        self.report_repository.report_inference(content, inference)

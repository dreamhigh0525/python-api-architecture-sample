from injector import inject
from src.domain.object.inference import Inference
from src.domain.repository.report_repository import AbstructReportRepository


class ReportService():
    report_repository: AbstructReportRepository

    @inject
    def __init__(self, report_repository: AbstructReportRepository):
        self.report_repository = report_repository

    async def report_inference(self, data: Inference) -> None:
        await self.report_repository.report_inference(data)

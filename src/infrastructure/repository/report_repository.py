from src.domain.object.inference import Inference
from src.domain.repository.report_repository import AbstructReportRepository


class ReportRepository(AbstructReportRepository):

    def __init__(self):
        pass

    async def report_inference(self, data: Inference) -> None:
        pass
    

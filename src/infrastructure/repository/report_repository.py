import requests
from src.domain.object.inference import Inference
from src.domain.repository.report_repository import AbstructReportRepository
from src.helper.api_module import logger


class ReportRepository(AbstructReportRepository):
    base_url: str

    def __init__(self):
        self.base_url = 'http://localhost:8080/report'

    def report_inference(self, data: Inference) -> None:
        res = requests.get(self.base_url)
        logger.info('report completed')

import requests
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.repository.report_repository import AbstractReportRepository
from inference.helper.api_module import logger


# TODO: implement
class ReportRepository(AbstractReportRepository):
    base_url: str

    def __init__(self):
        self.base_url = 'http://localhost:8080/report'

    def report_inference(self, content: Content, inference: Inference) -> None:
        res = requests.get(self.base_url)
        logger.info('report completed ' + str(res.content))

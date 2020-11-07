from typing import Tuple
from unittest import mock
import pytest
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.service.report_service import ReportService


class TestReportService:

    @pytest.fixture(scope='module')
    def result(mocker: mock) -> Tuple[Content, Inference]:
        with open('tests/test_image.jpg', 'rb') as f:
            image_data = f.read()
        result = (
            Content('test id', 'movie', 'http://localhost', image_data),
            Inference('0', 0.99)
        )
        return result

    def test_report_inference(self, mocker: mock, result: Tuple[Content, Inference]):
        repository_mock = mocker.MagicMock()
        repository_mock.report_inference = mocker.Mock(return_value=None)
        service = ReportService(repository_mock)
        service.report_inference(result[0], result[1])
        repository_mock.report_inference.assert_called_once_with(result[0], result[1])

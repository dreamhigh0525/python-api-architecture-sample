from typing import List
import pytest
from unittest import mock
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.object.inference_type import InferenceType
from inference.domain.service.inference_service import InferenceService


class TestInferenceService:

    @pytest.fixture(scope='module')
    def contents(mocker: mock) -> List[Content]:
        with open('tests/test_image.jpg', 'rb') as f:
            image_data = f.read()
        contents = [
            Content('test id', 'movie', 'http://localhost', image_data),
            Content('test id', 'gun', 'http://localhost', image_data)
        ]
        return contents

    def test_classifier_inference(self, mocker: mock, contents: List[Content]):
        repository_mock = mocker.MagicMock()
        repository_mock.get_inference = mocker.Mock(return_value=Inference('0', 0.99))
        service = InferenceService(repository_mock)
        inference = service.get_inference(contents[0])
        repository_mock.get_inference.assert_called_once_with(InferenceType.CLASSIFIER, contents[0])
        assert inference == Inference('0', 0.99)
    
    def test_detector_inference(self, mocker: mock, contents: List[Content]):
        repository_mock = mocker.MagicMock()
        repository_mock.get_inference = mocker.Mock(return_value=Inference('1', 0.89))
        service = InferenceService(repository_mock)
        inference = service.get_inference(contents[1])
        repository_mock.get_inference.assert_called_once_with(InferenceType.DETECTOR, contents[1])
        assert inference == Inference('1', 0.89)


from typing import List
from unittest import mock
import pytest
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.object.inference_type import InferenceType
from inference.infrastructure.repository.inference_repository import InferenceRepository


class TestInferenceRepository:

    @pytest.fixture(scope='function')
    def contents(self, mocker: mock) -> List[Content]:
        with open('tests/test_image.jpg', 'rb') as f:
            image_data = f.read()
        contents = [
            Content('test id', 'movie', 'http://localhost', image_data),
            Content('test id 2', 'gun', 'http://localhost', image_data)
        ]
        mocker.patch.object(
            InferenceRepository,
            '_InferenceRepository__set_model',
            return_value=None
        )
        return contents

    def test_get_inference_by_classifier(self, mocker: mock, contents: List[Content]):
        repository = InferenceRepository()
        result = (0, 0.99)
        repository.classifier = mocker.MagicMock()
        repository.classifier.predict = mocker.Mock(return_value=result)
        inference = repository.get_inference(InferenceType.CLASSIFIER, contents[0])
        assert inference == Inference(str(result[0]), result[1])
        repository.classifier.predict.assert_called_once_with(contents[0])

    def test_get_inference_by_detector(self, mocker: mock, contents: List[Content]):
        repository = InferenceRepository()
        result = (1, 0.99)
        repository.detector = mocker.MagicMock()
        repository.detector.predict = mocker.Mock(return_value=result)
        inference = repository.get_inference(InferenceType.DETECTOR, contents[1])
        assert inference == Inference(str(result[0]), result[1])
        repository.detector.predict.assert_called_once_with(contents[1])

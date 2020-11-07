import pytest
from unittest import mock
from responder import API
from inference.helper.api_module import api
from inference.application.inference_controller import InferenceController


class TestInferenceController:

    @pytest.fixture(scope='function')
    def api(self, mocker: mock) -> API:
        inference_service = mocker.MagicMock()
        report_service = mocker.MagicMock()
        inference_controller = InferenceController(inference_service, report_service)
        api.add_route('/inference', inference_controller.on_post, check_existing=False)
        mocker.patch.object(
            InferenceController,
            '_InferenceController__process_data',
            return_value=None
        )
        return api

    def test_inference_request(self, mocker: mock, api: API):
        image = open('tests/test_image.jpg', 'rb')
        data = {
            'id': (None, 1, 'text/plain'),
            'category': (None, 'gun', 'text/plain'),
            'url': (None, 'http://localhost/test.jpg', 'text/plain'),
            'file': ('test_image.jpg', image, 'image/jpeg')
        }
        ret = api.requests.post('/inference', files=data)
        assert ret.status_code == 202

    def test_validation_error(self, mocker: mock, api: API):
        image = open('tests/test_image.jpg', 'rb')
        data = {
            'id': (None, 1, 'text/plain'),
            'category': (None, 'gu', 'text/plain'),
            'url': (None, 'http://localhost/test.jpg', 'text/plain'),
            'file': ('test_image.jpg', image, 'image/jpeg')
        }
        ret = api.requests.post('/inference', files=data)
        assert ret.status_code == 400
        data['category'] = (None, 'movie', 'text/plain')
        del data['file']
        ret = api.requests.post('/inference', files=data)
        assert ret.status_code == 400


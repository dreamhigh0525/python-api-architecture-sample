import pytest
from bin import app


@pytest.fixture
def api():
    return app.api


def test_inference(api):
    filename = 'tests/test_image.jpg'
    image_file = open(filename, 'rb').read()
    files = {
        'id': (None, 'test id', 'text/plain'),
        'file': (filename, image_file, 'image/jpeg'),
        'category': (None, 'movie', 'text/plain'),
        'url': (None, 'https://localhost/test.jpg', 'text/plain')
    }
    r = api.requests.post('/inference', files=files)
    assert r.status_code == 202


def test_report(api):
    r = api.requests.get('/report')
    assert r.status_code == 200

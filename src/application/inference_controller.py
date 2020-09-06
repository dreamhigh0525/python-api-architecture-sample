from injector import Injector
from responder.api import API
from src.domain.object.image import Image
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.domain.service.inference_service import InferenceService


class InferenceController:
    inference_service: InferenceService
    api: API

    def __init__(self, api: API, injector: Injector):
        repository = injector.get(AbstructInferenceRepository)
        self.inference_service = InferenceService(
            inference_repository=repository
        )
        self.api = api

    async def on_get(self, req, res):
        res.media = {"id": 'test id', "confidence": 1.0}

    async def on_post(self, req, res):
        api = self.api
        @api.background.task
        async def process_data(data):
            image = Image(id=data['id'], data=data['content'])
            result = await self.inference_service.get_inference(image)
            print(result)

        data = await req.media(format='files')
        process_data(data)
        res.status_code = 202
        res.media = {'status': 'ok'}

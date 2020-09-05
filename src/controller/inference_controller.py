from responder.api import API
from src.model.image import Image
from src.service.inference_service import InferenceService


class InferenceController:
    inference_service: InferenceService
    api: API

    def __init__(self, api: API):
        print("init")
        self.inference_service = InferenceService()
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
        
        
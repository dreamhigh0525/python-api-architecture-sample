import sys
from responder import Request, Response
from marshmallow.exceptions import ValidationError
from src.domain.object.image import Image
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.domain.service.inference_service import InferenceService
from src.application.request_schema import InferenceRequest, InferenceRequestSchema
from src.helper.api_module import api
from src.helper.di_module import injector


class InferenceController:
    inference_service: InferenceService

    def __init__(self):
        repository = injector.get(AbstructInferenceRepository)
        self.inference_service = InferenceService(
            inference_repository=repository
        )

    async def on_get(self, req: Request, res: Response):
        res.media = {'status': 'ok'}

    async def on_post(self, req: Request, res: Response):
        """Inference Service
        ---
        post:
          summary: image inference service
          description: post a image file for inference
          requestBody:
            content:
              multipart/form-data:
                schema:
                  type: object
                  properties:
                    id:
                      type: string
                      required: true
                    file:
                      type: string
                      format: binary
                      required: true
          responses:
            202:
              description: request accepted
              schema:
                type: object
                properties:
                  status:
                    type: string
            400:
              description: invalid parameters
            500:
              description: internal server error
        """
        try:
            data = await req.media(format='files')
            schema = InferenceRequestSchema().load(data)
            self.__process_data(schema)
            res.status_code = 202
            res.media = {'status': f'request accepted: {schema.id}'}
        except ValidationError as e:
            res.status_code = 400
            res.media = {'message': e.messages}
            print(e, file=sys.stderr)

    @api.background.task
    async def __process_data(self, req: InferenceRequest):
        image = Image(id=req.id, data=req.file['content'])
        result = await self.inference_service.get_inference(image)
        print(result)

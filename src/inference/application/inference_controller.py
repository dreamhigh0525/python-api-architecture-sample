from injector import inject
from responder import Request, Response
from marshmallow.exceptions import ValidationError
from inference.application.request_schema import InferenceRequest, InferenceRequestSchema
from inference.domain.object.content import Content
from inference.domain.service.inference_service import InferenceService
from inference.domain.service.report_service import ReportService
from inference.helper.api_module import api, logger


class InferenceController:
    inference_service: InferenceService
    report_service: ReportService

    @inject
    def __init__(self, inference_service: InferenceService, report_service: ReportService):
        self.inference_service = inference_service
        self.report_service = report_service

    async def on_get(self, req: Request, res: Response):
        res.media = {'status': 'ok'}  # type: ignore

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
                      example: test id
                    file:
                      type: string
                      format: binary
                      required: true
                      example: image file binary
                    category:
                      type: string
                      required: true
                      example: movie|gun
                    url:
                      type: string
                      required: true
                      example: https://localhost/test.jpg
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
            schema = InferenceRequestSchema().load(data, many=False)
            self.__process_data(schema)
            res.status_code = 202
            res.media = {'status': f'request accepted: {schema.id}'}  # type: ignore
            logger.debug(f'request accepted: {schema.id}')
        except ValidationError as e:
            res.status_code = 400
            res.media = {'message': e.messages}  # type: ignore
            logger.warn(e.messages)

    @api.background.task
    def __process_data(self, req: InferenceRequest):
        content = Content(
            id=req.id,
            category=req.category,
            url=req.url,
            data=req.file['content']
        )
        result = self.inference_service.get_inference(content)
        logger.info(f':{content.id}\t{content.category}\t{content.url}\t{result.label}\t{result.confidence}')
        self.report_service.report_inference(content, result)

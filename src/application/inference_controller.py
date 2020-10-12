from responder import Request, Response
from marshmallow.exceptions import ValidationError
from src.application.request_schema import InferenceRequest, InferenceRequestSchema
from src.domain.object.content import Content
from src.domain.object.inference_type import InferenceType
from src.domain.service.inference_service import InferenceService
from src.domain.service.report_service import ReportService
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.domain.repository.report_repository import AbstructReportRepository
from src.helper.api_module import api, logger
from src.helper.di_module import injector


class InferenceController:
    inference_service: InferenceService
    report_service: ReportService

    def __init__(self):
        inference_repository = injector.get(AbstructInferenceRepository)
        self.inference_service = InferenceService(
            inference_repository=inference_repository
        )
        report_repository = injector.get(AbstructReportRepository)
        self.report_service = ReportService(
            report_repository=report_repository
        )

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
                    type:
                      type: string
                      required: true
                      example: movie|gun
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
            logger.info(f'request accepted: {schema.id}')
        except ValidationError as e:
            res.status_code = 400
            res.media = {'message': e.messages}  # type: ignore
            logger.warn(e.messages)

    @api.background.task
    def __process_data(self, req: InferenceRequest):
        content = Content(
            id=req.id,
            filename=req.file['filename'],
            data=req.file['content']
        )
        if req.type == 'movie':
            type = InferenceType.CLASSIFIER
        else:
            type = InferenceType.DETECTOR

        result = self.inference_service.get_inference(type, content)
        logger.info(result)
        self.report_service.report_inference(result)

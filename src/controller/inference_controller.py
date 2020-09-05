from src.infrastructure.inference_driver import InferenceDriver
from src.interactor.inference_interactor import InferenceInteractor
from src.repository.inference_repository import InferenceRepository
from src.resource.inference_resource import InferenceResource


class InferenceController:
    inference_resource: InferenceResource

    def __init__(self):
        print("init")
        self.inference_resource = InferenceResource(
            inference_usecase=InferenceInteractor(
                inference_repository=InferenceRepository(
                    inference_driver=InferenceDriver()
                )
            )
        )

    async def on_get(self, req, res, *, id):
        result = await self.inference_resource.get_inference()
        res.media = {"id": result.id, "confidence": result.confidence}




from src.model.inference import Inference
from src.model.image import Image
from src.repository.inference_repository import InferenceRepository


class InferenceService():
    inference_repository: InferenceRepository

    def __init__(self):
        self.inference_repository = InferenceRepository()

    async def get_inference(self, image: Image) -> Inference:
        return await self.inference_repository.get_inference(image.data)

from src.model.inference import Inference
from src.repository.inference_repository import InferenceRepository


class InferenceService():
    inference_repository: InferenceRepository

    def __init__(self):
        self.inference_repository = InferenceRepository()

    async def get_inference(self) -> Inference:
        return await self.inference_repository.get_inference()

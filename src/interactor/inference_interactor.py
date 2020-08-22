from src.domain.inference import Inference
from src.interface.inference_repository import AbstractInferenceRepository
from src.interface.inference_usecase import InferenceUseCase


class InferenceInteractor(InferenceUseCase):
    inference_repository: AbstractInferenceRepository

    def __init__(self, inference_repository: AbstractInferenceRepository):
        self.inference_repository = inference_repository

    async def get_inference(self) -> Inference:
        return await self.inference_repository.get_inference()

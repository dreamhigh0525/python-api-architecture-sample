from src.domain.inference import Inference
from src.interface.inference_usecase import InferenceUseCase


class InferenceResource:
    inference_usecase: InferenceUseCase

    def __init__(self, inference_usecase: InferenceUseCase):
        self.inference_usecase = inference_usecase

    async def on_get(self) -> Inference:
        inference = await self.inference_usecase.get_inference()
        return inference

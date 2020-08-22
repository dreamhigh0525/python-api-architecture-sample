from src.domain.inference import Inference
from src.interface.inference_driver import AbstractInferenceDriver
from src.interface.inference_repository import AbstractInferenceRepository


class InferenceRepository(AbstractInferenceRepository):
    inference_driver: AbstractInferenceDriver

    def __init__(self, inference_driver: AbstractInferenceDriver):
        self.inference_driver = inference_driver

    async def get_inference(self) -> Inference:
        res = await self.inference_driver.get_inference()
        return Inference(id=res[0], confidence=res[1])


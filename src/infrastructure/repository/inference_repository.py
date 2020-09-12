import asyncio
from src.domain.object.image import Image
from src.domain.object.inference import Inference
from src.domain.repository.inference_repository import AbstructInferenceRepository


class InferenceRepository(AbstructInferenceRepository):

    def __init__(self):
        pass

    async def get_inference(self, data: Image) -> Inference:
        await asyncio.sleep(3)
        res = ('test id', 1.0)
        return Inference(id=res[0], confidence=res[1])


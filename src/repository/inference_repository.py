import asyncio
from src.model.inference import Inference


class InferenceRepository:

    def __init__(self):
        pass

    async def get_inference(self) -> Inference:
        await asyncio.sleep(3)
        res = ('test id', 1.0)
        return Inference(id=res[0], confidence=res[1])


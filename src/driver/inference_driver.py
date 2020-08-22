import asyncio
from typing import Tuple
from src.interface.inference_driver import AbstractInferenceDriver


class InferenceDriver(AbstractInferenceDriver):
    async def get_inference(self) -> Tuple[str, float]:
        await asyncio.sleep(3)  # access another resources
        return ('test id', 1.0)


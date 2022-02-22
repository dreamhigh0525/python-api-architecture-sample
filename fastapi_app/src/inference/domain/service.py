from fastapi import Depends
from .content import Content
from .inference import Inference
from .inference_type import InferenceType
from .repository import InferenceRepository
from ..infrastructure.proxy import Proxy


class InferenceService:
    repository: InferenceRepository

    def __init__(self, repository: InferenceRepository = Depends(Proxy)):
        self.repository = repository

    async def get_inference(self, content: Content) -> Inference:
        type = InferenceType.CLASSIFIER
        return await self.repository.get_inference(type, content)

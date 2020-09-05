from src.service.inference_service import InferenceService


class InferenceController:
    inference_service: InferenceService

    def __init__(self):
        print("init")
        self.inference_service = InferenceService()

    async def on_get(self, req, res, *, id):
        result = await self.inference_service.get_inference()
        res.media = {"id": result.id, "confidence": result.confidence}

from injector import inject
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.repository.inference_repository import AbstructInferenceRepository


class InferenceService():
    inference_repository: AbstructInferenceRepository

    @inject
    def __init__(self, inference_repository: AbstructInferenceRepository):
        self.inference_repository = inference_repository

    def get_inference(self, image: Content) -> Inference:
        return self.inference_repository.get_inference(image)

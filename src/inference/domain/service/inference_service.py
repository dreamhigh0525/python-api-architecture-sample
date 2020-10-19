from injector import inject
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.object.inference_type import InferenceType
from inference.domain.repository.inference_repository import AbstractInferenceRepository


class InferenceService():
    inference_repository: AbstractInferenceRepository

    @inject
    def __init__(self, inference_repository: AbstractInferenceRepository):
        self.inference_repository = inference_repository

    def get_inference(self, content: Content) -> Inference:
        if content.category == 'movie':
            type = InferenceType.CLASSIFIER
        else:  # category == gun
            type = InferenceType.DETECTOR
        return self.inference_repository.get_inference(type, content)

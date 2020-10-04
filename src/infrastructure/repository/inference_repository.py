import time
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.infrastructure.repository.classifier import Classifier


class InferenceRepository(AbstructInferenceRepository):
    classifier: Classifier

    def __init__(self):
        model_path = './static/model_epoch_110_NSFW.pth'
        self.classifier = Classifier(model_path)

    def get_inference(self, image: Content) -> Inference:
        label, confidence = self.classifier.predict(image)
        return Inference(id=str(label), confidence=confidence)


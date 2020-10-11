from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.object.inference_type import InferenceType
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.infrastructure.repository.classifier import Classifier
from src.infrastructure.repository.detector import Detector


class InferenceRepository(AbstructInferenceRepository):
    classifier: Classifier
    detector: Detector

    def __init__(self):
        # TODO: refactoring
        classifier_model_path = './static/model_epoch_110_NSFW.pth'
        detector_model_path = './static/model_epoch_75_Guns.pth'
        self.classifier = Classifier(classifier_model_path)
        self.detector = Detector(detector_model_path)

    def get_inference(self, type: InferenceType, image: Content) -> Inference:
        if type == InferenceType.CLASSIFIER:
            label, confidence = self.classifier.predict(image)
        else:
            label, confidence = self.detector.predict(image)
        
        return Inference(label=str(label), confidence=confidence)

import os
from src.domain.object.content import Content
from src.domain.object.inference import Inference
from src.domain.object.inference_type import InferenceType
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.infrastructure.repository.classifier import Classifier
from src.infrastructure.repository.detector import Detector
from src.infrastructure.repository.exceptions import ModelNotFoundError
from src.helper.api_module import logger


class InferenceRepository(AbstructInferenceRepository):
    classifier: Classifier
    detector: Detector

    def __init__(self):
        # TODO: adapt for paas (No space left on device)
        self.__set_model()

    def get_inference(self, type: InferenceType, content: Content) -> Inference:
        if type == InferenceType.CLASSIFIER:
            label, confidence = self.classifier.predict(content)
        else:
            label, confidence = self.detector.predict(content)

        return Inference(label=str(label), confidence=confidence)

    def __set_model(self):
        try:
            base_path = 'static/'
            classifier_model = base_path + os.environ['CLASSIFIER_MODEL']
            self.classifier = Classifier(classifier_model)
            detector_model = base_path + os.environ['DETECTOR_MODEL']
            if os.environ.get('VCAP_APPLICATION') is None:
                # [Errno 28] no space left on device
                self.detector = self.classifier  # type: ignore
            else:
                self.detector = Detector(detector_model)
        except KeyError as e:
            logger.critical(e.args[0] + ' key not found')
            raise ModelNotFoundError(e)

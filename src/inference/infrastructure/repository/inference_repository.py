import os
from inference.domain.object.content import Content
from inference.domain.object.inference import Inference
from inference.domain.object.inference_type import InferenceType
from inference.domain.repository.inference_repository import AbstractInferenceRepository
from inference.infrastructure.repository.classifier import Classifier
from inference.infrastructure.repository.detector import Detector
from inference.infrastructure.repository.exceptions import ModelNotFoundError
from inference.helper.api_module import logger


# TODO: adapt for PaaS (No space left on device)
class InferenceRepository(AbstractInferenceRepository):
    classifier: Classifier
    detector: Detector

    def __init__(self):
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
                self.detector = Detector(detector_model)
            else:
                self.detector = self.classifier  # type: ignore
                
        except KeyError as e:
            logger.critical(e.args[0] + ' key not found')
            raise ModelNotFoundError(e)

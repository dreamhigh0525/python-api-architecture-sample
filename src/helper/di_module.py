from injector import Injector, Module
from src.domain.repository.inference_repository import AbstructInferenceRepository
from src.infrastructure.repository.inference_repository import InferenceRepository


class InferenceDIModule(Module):
    def configure(self, binder):
        binder.bind(AbstructInferenceRepository, to=InferenceRepository)


injector = Injector([InferenceDIModule()])

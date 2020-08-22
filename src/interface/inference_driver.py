from abc import ABCMeta, abstractmethod
from typing import Tuple


class AbstractInferenceDriver(metaclass=ABCMeta):
    @abstractmethod
    async def get_inference(self) -> Tuple[str, float]:
        raise NotImplementedError

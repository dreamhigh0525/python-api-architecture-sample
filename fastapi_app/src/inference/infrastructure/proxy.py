import requests
from requests import Response
from ..domain.content import Content
from ..domain.inference import Inference
from ..domain.inference_type import InferenceType
from ..domain.repository import InferenceRepository

import time

class Proxy(InferenceRepository):
    entry_point: str = 'https://jsonplaceholder.typicode.com/posts/'

    def __init__(self):
        super().__init__()
        
    async def get_inference(self, type: InferenceType, content: Content) -> Inference:
        image = content.get_pil_image()
        response = requests.post(self.entry_point, data={'a':'b'})
        time.sleep(1)
        print(response.content)
        return Inference(label='label', confidence=1.0)

    def convert_response(self, res: Response):
        raise NotImplementedError

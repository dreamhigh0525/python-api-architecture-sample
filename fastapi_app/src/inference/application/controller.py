from fastapi import APIRouter, Depends
from ..domain.content import Content
from ..domain.inference import Inference
from ..domain.service import InferenceService

router = APIRouter()


@router.get('/', response_model=dict[str, str])
async def check() -> dict[str, str]:
    return {'status': 'ok'}


@router.post('/inference',  response_model=Inference)
async def inference(
    content: Content = Depends(),
    service: InferenceService = Depends()
) -> Inference:
    inference = await service.get_inference(content)
    return inference

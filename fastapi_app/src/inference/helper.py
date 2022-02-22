from fastapi import FastAPI
from fastapi import Form
from fastapi.openapi.utils import get_openapi

# fastapi 0.7ではmultipart/form-dataのModelには未対応のため拡張
# https://github.com/tiangolo/fastapi/issues/2387
# https://stackoverflow.com/questions/60127234/how-to-use-a-pydantic-model-with-form-data-in-fastapi
def as_form(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

# 自動生成されたOpenAPI(Swagger)仕様を一部修正
def extend_schema(api: FastAPI):
    schema = get_openapi(
        title='Image Inference API',
        version='1.0.0',
        routes=api.routes
    )
    schema['paths']['/inference']['post']['requestBody']['content'] = {
        'multipart/form-data': {'schema': {'$ref': '#/components/schemas/Body_inference_inference_post'}}
    }
    api.openapi_schema = schema


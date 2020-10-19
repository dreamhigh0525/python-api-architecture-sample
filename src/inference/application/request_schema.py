from dataclasses import dataclass
from typing import Any, Dict
from marshmallow import Schema, fields, post_load
from marshmallow.exceptions import ValidationError


@dataclass(frozen=True)
class InferenceRequest:
    id: str
    file: Dict[str, Any]
    category: str
    url: str


# multipart/form-data
class InferenceRequestSchema(Schema):
    id = fields.Dict(required=True)
    file = fields.Dict(required=True)
    category = fields.Dict(required=True)
    url = fields.Dict(required=True)

    @post_load
    def make_object(self, data, **kwargs) -> InferenceRequest:
        id = data['id']['content'].decode('utf-8')
        image_file: Dict = data['file']
        if not isinstance(image_file['content'], bytes):
            raise ValidationError('file must be a image binary file')
        category = str(data['category']['content'].decode('utf-8'))
        if category not in ['movie', 'gun']:
            raise ValidationError('category must be movie or gun')
        url = str(data['url']['content'].decode('utf-8'))

        return InferenceRequest(
            id=id,
            file=image_file,
            category=category,
            url=url
        )

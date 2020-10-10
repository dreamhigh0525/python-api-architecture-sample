from dataclasses import dataclass
from typing import Any, Dict
from marshmallow import Schema, fields, post_load
from marshmallow.exceptions import ValidationError


@dataclass(frozen=True)
class InferenceRequest:
    id: str
    file: Dict[str, Any]
    type: str


class InferenceRequestSchema(Schema):
    id = fields.Dict(required=True)
    file = fields.Dict(required=True)
    type = fields.Dict(required=True)

    @post_load
    def make_object(self, data, **kwargs) -> InferenceRequest:
        id = data['id']['content'].decode('utf-8')
        image_file: Dict = data['file']
        if not isinstance(image_file['content'], bytes):
            raise ValidationError('file must be a image binary file')
        content_type = str(data['type']['content'].decode('utf-8'))
        if content_type not in ['movie', 'gun']:
            raise ValidationError('type must be movie or gun')
        return InferenceRequest(
            id=id,
            file=image_file,
            type=content_type
        )

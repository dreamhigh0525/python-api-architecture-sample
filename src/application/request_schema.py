from dataclasses import dataclass
from typing import Any, Dict
from marshmallow import Schema, fields, post_load
from marshmallow.exceptions import ValidationError


@dataclass(frozen=True)
class InferenceRequest:
    id: str
    file: Dict[str, Any]


class InferenceRequestSchema(Schema):
    id = fields.String(required=True)
    file = fields.Dict(required=True)

    @post_load
    def make_object(self, data, **kwargs) -> InferenceRequest:
        image_file: Dict = data['file']
        if not isinstance(image_file['content'], bytes):
            raise ValidationError('file must be a image binary file')
        return InferenceRequest(**data)

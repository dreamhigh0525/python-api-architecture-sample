from typing import Union
from io import BytesIO
from fastapi import File, Form, UploadFile
from pydantic import BaseModel, validator
from PIL import Image, ImageFile
from PIL.Image import Image as PILImage
from ..helper import as_form

ImageFile.LOAD_TRUNCATED_IMAGES = True  # type: ignore


@as_form
class Content(BaseModel):
    id: str = Form(..., title='content id')
    category: str = Form(..., title='content category')
    image: UploadFile = File(..., title='content image file')

    @validator('image')
    def check_image_type(cls, image: UploadFile) -> Union[UploadFile, ValueError]:
        if not image.content_type == 'image/jpeg':
            raise ValueError('content-type must be image/jpeg')
        return image
    
    def get_pil_image(self) -> PILImage:
        return Image.open(BytesIO(self.image.file.read())).convert('RGB')

    class Config:
        title = 'Content'
        arbitrary_types_allowed = True
    

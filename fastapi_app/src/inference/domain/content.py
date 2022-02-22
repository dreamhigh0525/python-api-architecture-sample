from io import BytesIO
from fastapi import File, Form, UploadFile
from pydantic import BaseModel
from PIL import Image, ImageFile
from PIL.Image import Image as PILImage
from ..helper import as_form

ImageFile.LOAD_TRUNCATED_IMAGES = True  # type: ignore


@as_form
class Content(BaseModel):
    id: str = Form(None, title='content id')
    category: str = Form(..., title='content category')
    image: UploadFile = File(..., title='content image file')

    def get_pil_image(self) -> PILImage:
        return Image.open(BytesIO(self.image.file.read())).convert('RGB')

    class Config:
        title = 'Content'
        arbitrary_types_allowed = True
    

from dataclasses import dataclass
from io import BytesIO
from PIL import Image, ImageFile
from PIL.Image import Image as PILImage
ImageFile.LOAD_TRUNCATED_IMAGES = True  # type: ignore


@dataclass(frozen=True)
class Content:
    id: str
    filename: str
    data: PILImage

    def __init__(self, id: str, filename: str, data: bytes):
        object.__setattr__(self, 'id', id)
        object.__setattr__(self, 'filename', filename)
        object.__setattr__(self, 'data', Image.open(BytesIO(data)))
        self.data.convert('RGB')

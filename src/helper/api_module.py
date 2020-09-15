
import responder
from logging import getLogger, FileHandler, StreamHandler, DEBUG

api = responder.API(
    openapi='3.0.0',
    title="Image Inference API",
    docs_route='/docs',
    version='0.0.1'
)

logger = getLogger(__name__)
file_handler = FileHandler('request.log')
file_handler.setLevel(DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(DEBUG)
#file_handler.setFormatter()
#stream_handler.setFormatter()

logger.setLevel(DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate = False

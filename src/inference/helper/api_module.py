
import responder
from logging import getLogger, Formatter, FileHandler, StreamHandler, INFO

api = responder.API(
    openapi='3.0.0',
    title="Image Inference API",
    docs_route='/docs',
    version='0.0.1'
)

logger = getLogger(__name__)
formatter = Formatter('%(asctime)s [%(levelname)s] :%(message)s')
file_handler = FileHandler('request.log')
file_handler.setLevel(INFO)
file_handler.setFormatter(formatter)
stream_handler = StreamHandler()
stream_handler.setLevel(INFO)
stream_handler.setFormatter(formatter)

logger.setLevel(INFO)
# logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.propagate = False

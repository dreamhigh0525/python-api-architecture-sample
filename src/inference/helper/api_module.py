import os
import responder
from logging import getLogger, Formatter, StreamHandler, INFO
from logging.handlers import TimedRotatingFileHandler

api = responder.API(
    openapi='3.0.0',
    title="Image Inference API",
    docs_route='/docs',
    version='0.0.1'
)


logger = getLogger(__name__)
logger.setLevel(INFO)
formatter = Formatter('%(asctime)s [%(levelname)s] :%(message)s')
if os.environ.get('GITHUB_ACTIONS') is None:  # for Github Actions
    filename = os.environ.get('LOG_PATH', 'logs/access.log')
    file_handler = TimedRotatingFileHandler(
        filename=filename,
        when='midnight',
        backupCount=7,
        encoding='utf-8'
    )
    file_handler.setLevel(INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

stream_handler = StreamHandler()
stream_handler.setLevel(INFO)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.propagate = False

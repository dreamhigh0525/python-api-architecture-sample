#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.helper.api_module import api, logger
from src.application.inference_controller import InferenceController
from src.application.exception import exception_handler

try:
    controller = InferenceController()
    api.add_route('/inference', controller.on_post)
    api.add_route('/report', controller.on_get)
    api.add_route('/', exception_handler, default=True)
except KeyError as e:
    logger.critical(e.args[0] + ' key not found, cannot loading model')

if __name__ == '__main__':
    api.run(port=8080, debug=True)

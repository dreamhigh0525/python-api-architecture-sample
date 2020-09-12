#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.helper.api_module import api
from src.application.inference_controller import InferenceController
from src.application.exception import exception_handler


controller = InferenceController()
api.add_route('/', endpoint=exception_handler, default=True)
api.add_route('/inference', controller.on_post)

if __name__ == '__main__':
    api.run(port=8080, debug=True)

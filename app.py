#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from src.helper.api_module import api
from src.application.inference_controller import InferenceController
from src.application.exception import exception_handler

controller = InferenceController()
api.add_route('/inference', controller.on_post)
api.add_route('/report', controller.on_get)
api.add_route('/', exception_handler, default=True)

if __name__ == '__main__':
    port = os.environ.get('PORT', 80)
    debug = os.environ.get('DEBUG', False)
    api.run(port=port, debug=debug)

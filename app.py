#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from inference.helper.api_module import api
from inference.application.inference_controller import InferenceController
from inference.application.exception import exception_handler
from inference.helper.di_module import injector

controller = injector.get(InferenceController)
api.add_route('/inference', controller.on_post)
api.add_route('/report', controller.on_get)
api.add_route('/', exception_handler, default=True)


if __name__ == '__main__':
    port = os.environ.get('PORT', 80)
    debug = os.environ.get('DEBUG', False)
    api.run(address="0.0.0.0", port=port, debug=debug)

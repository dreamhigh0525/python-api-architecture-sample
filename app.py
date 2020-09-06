#!/usr/bin/env python
# -*- coding: utf-8 -*-

import responder
from src.application.inference_controller import InferenceController
from src.helper.di_module import injector

if __name__ == '__main__':
    api = responder.API()
    controller = InferenceController(api, injector)
    api.add_route("/inference", controller.on_post)

    api.run(port=8080, debug=True)

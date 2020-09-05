#!/usr/bin/env python
# -*- coding: utf-8 -*-

import responder
from src.controller.inference_controller import InferenceController

api = responder.API()
controller = InferenceController()

api.add_route("/inference/{id:int}", controller.on_get)

if __name__ == '__main__':
    api.run(port=8080, debug=True)

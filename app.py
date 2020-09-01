#!/usr/bin/env python
# -*- coding: utf-8 -*-

import responder
from src.controller.inference_controller import InferenceController

api = responder.API()

api.add_route("/inference/{id:int}", InferenceController)

if __name__ == '__main__':
    api.run(port=8080, debug=True)

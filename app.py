#!/usr/bin/env python
# -*- coding: utf-8 -*-

import responder
from src.driver.inference_driver import InferenceDriver
from src.interactor.inference_interactor import InferenceInteractor
from src.repository.inference_repository import InferenceRepository
from src.resource.inference_resource import InferenceResource


api = responder.API()

inference_resource = InferenceResource(
    inference_usecase=InferenceInteractor(
        inference_repository=InferenceRepository(
            inference_driver=InferenceDriver()
        )
    )
)


@api.route("/inference")
async def inference(req, res):
    result = await inference_resource.on_get()
    res.media = {"id": result.id, "confidence": result.confidence}


if __name__ == '__main__':
    api.run()

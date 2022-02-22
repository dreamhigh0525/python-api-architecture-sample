#!/usr/bin/env python

import os
from fastapi import FastAPI
import uvicorn
from .application.controller import router
from .helper import extend_schema


api = FastAPI()
api.include_router(router)
extend_schema(api)

def start():
    uvicorn.run(
        "src.inference.app:api",
        host=os.environ.get('HOST', '127.0.0.1'),
        port=int(os.environ.get('PORT', 8080)),
        log_level="info",
        reload=True
    )


if __name__ == '__main__':
    start()


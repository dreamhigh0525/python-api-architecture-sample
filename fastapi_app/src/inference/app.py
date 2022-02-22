#!/usr/bin/env python

from fastapi import FastAPI
from .application.controller import router
from .helper import extend_schema
import uvicorn
from pprint import pprint

api = FastAPI()
api.include_router(router)
extend_schema(api)

def start(host: str="127.0.0.1", port: int=8888):
    uvicorn.run(
        "src.inference.app:api",
        host=host,
        port=port,
        log_level="info",
        reload=True
    )


if __name__ == '__main__':
    start()


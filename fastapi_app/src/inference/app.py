#!/usr/bin/env python

import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from .application.controller import router
from .helper import extend_schema


api = FastAPI()
api.include_router(router)
extend_schema(api)

@api.exception_handler(ValueError)
async def error_handler(request: Request, error: ValueError):
    return JSONResponse(status_code=400, content={"message": str(error)})


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


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def set_exceptions(api: FastAPI):
    @api.exception_handler(ValueError)
    async def error_handler(request: Request, error: ValueError):
        return JSONResponse(status_code=400, content={"message": str(error)})

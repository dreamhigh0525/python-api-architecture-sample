#!/usr/bin/env python

import os
import uvicorn


def start():
    uvicorn.run(
        "src.inference.app:api",
        host=os.environ.get('HOST', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        log_level="info",
        reload=True
    )


if __name__ == '__main__':
    start()

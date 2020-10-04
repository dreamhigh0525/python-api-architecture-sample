from responder import Request, Response


def exception_handler(req: Request, res: Response):
    res.status_code = 404
    res.media = {'status': 'endpoint not found error'}
        

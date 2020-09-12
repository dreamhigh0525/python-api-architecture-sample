
def exception_handler(req, res):
    res.status_code = 404
    res.media = {'status': 'endpoint not found error'}
        

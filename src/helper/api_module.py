import responder

api = responder.API(
    openapi='3.0.0',
    title="Image Inference API",
    docs_route='/docs',
    version='0.0.1'
)

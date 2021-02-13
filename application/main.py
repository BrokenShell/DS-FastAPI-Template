from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application import predict


application = FastAPI(
    title='DS FastAPI Test',
    description='This is just a test.',
    version='0.1',
    docs_url='/',
)

application.include_router(predict.router)

application.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from application import predict


application = FastAPI(
    title='DS FastAPI Template',
    description='This is just a test.',
    version='0.1.1',
    docs_url='/',
)

application.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@application.get("/version")
async def version():
    return {"version": application.version}


application.include_router(predict.router)

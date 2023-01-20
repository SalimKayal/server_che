from fastapi import APIRouter
from fastapi import FastAPI

router = APIRouter()

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
)


@router.get('/hello')
def hello(request):
    return "hello"+request


app.include_router(router)

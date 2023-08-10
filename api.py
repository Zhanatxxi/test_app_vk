from fastapi import FastAPI
from uvicorn import run

from vk_app.view import app_router

app = FastAPI(
    title="VK parser",
    description="mini Technical task for vk parsing about profile"
)


@app.get("/")
def welcome():
    return "Welcome!"


app.include_router(app_router, prefix="/api/v1")


if __name__ == '__main__':
    run("api:app", workers=1, reload=True, host='0.0.0.0')



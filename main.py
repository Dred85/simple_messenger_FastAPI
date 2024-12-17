from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from routers import users, messages
from fastapi import Request

app = FastAPI()

app.include_router(users.router)
app.include_router(messages.router)


@app.get("/")
async def root():
    return {"message": "Приложение работает"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
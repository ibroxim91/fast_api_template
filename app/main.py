from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn





@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
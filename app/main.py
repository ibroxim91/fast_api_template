from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from .routes import company_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(company_router, prefix="/company", tags=["company"])

@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
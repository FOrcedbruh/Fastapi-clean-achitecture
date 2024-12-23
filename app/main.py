from fastapi import FastAPI, HTTPException
import uvicorn
from config import settings
from presentation import router as MainRouter
from fastapi.middleware.cors import CORSMiddleware
from repositories.exceptions import NotFoundError




app = FastAPI(
    title="Clean Architecture API with FastAPI"
)

app.include_router(router=MainRouter)
app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)


@app.get("/")
def index():
    return {
        "message": "Hello"
    }


@app.exception_handler(NotFoundError)
def index(requset, exc: NotFoundError):
    raise HTTPException(
        status_code=exc.status_code,
        detail=exc.message
    )




if __name__ == "__main__":
    uvicorn.run(app="main:app", port=settings.runcfg.port, host=settings.runcfg.host, reload=bool(settings.runcfg.reload))

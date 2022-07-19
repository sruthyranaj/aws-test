import uvicorn
from fastapi import FastAPI, APIRouter

# Initialize app instance
app = FastAPI(title="Demo",
              description="Demo App",
              version="V1.0.0",
              docs_url="/docs")


router = APIRouter(prefix="/api")


@router.get("/test")
def app_version():
    return {"data": {"status": "Success"}}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)

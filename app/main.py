from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

@app.get("/app/health")
def health_check():
    return {"status" : "healthy",
            "message" : "The application is running smoothly."
            }
    

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils import log
from app.api.endpoints import router as api_router

app = FastAPI()

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the API router
app.include_router(api_router)

@app.get("/")
def read_root():
    log(stack="backend", level="info", pkg="route", message="read_root called")
    return {"message": "Welcome to the URL Shortener API!"}
 
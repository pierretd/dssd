from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_env = os.getenv("API_ENV", "production")
debug = os.getenv("DEBUG", "False").lower() == "true"

app = FastAPI(
    title="FastAPI Backend",
    description="Backend API for the application",
    version="0.1.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json",
    debug=debug
)

# Add CORS middleware to allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(items.router)

@app.get("/api/hello")
async def hello_world():
    return {"message": f"Hello from FastAPI ({api_env} environment)"}

@app.get("/")
async def root():
    return {"message": "Welcome to the API. Visit /api/docs for documentation."} 
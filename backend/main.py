# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
# This must happen before anything else reads os.environ
load_dotenv()

# Create the FastAPI app instance
# This is the object that holds all your routes and config
app = FastAPI(
    title="AI Job Autopilot API",
    description="Backend for the AI Job Application Autopilot project",
    version="1.0.0"
)

# ─── CORS Configuration ───────────────────────────────────────────────────────
# This tells FastAPI to allow requests from your React frontend
# Without this, the browser will block all API calls from React

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.get("/")
def root():
    """Root route — just confirms the server is running"""
    return {
        "message": "AI Job Autopilot API is running",
        "status": "ok",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """
    Health check route.
    In real companies, monitoring tools ping this every few minutes
    to confirm the server is alive. Good habit to always include it.
    """
    return {
        "status": "healthy",
        "environment": os.getenv("APP_ENV", "development")
    }

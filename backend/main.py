"""
Main application entry point for the RegretNet AI backend.

This file initializes the FastAPI app, loads environment variables,
registers API routes, and starts the server.
"""
from services.logger import setup_logger

setup_logger()

from fastapi import FastAPI
from api.simulate import router as simulate_router

app = FastAPI(title="RegretNet AI", version="1.0")

# Register API routes
app.include_router(simulate_router)

@app.get("/")
def health_check():
    """
    Health check endpoint to verify that the backend is running.

    Returns:
        dict: Status message.
    """
    return {"status": "RegretNet backend is running"}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


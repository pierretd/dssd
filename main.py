from app.main import app

# This entry point file is needed for production deployment
# It imports the app from the app package and re-exports it for uvicorn

if __name__ == "__main__":
    import uvicorn
    # Run the application with uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

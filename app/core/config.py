import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="app/core/enviroment/.env_app")

API_VERSION = "v1"
API_STR = f"/api/{API_VERSION}"
API_V1_STR = f"/api/{API_VERSION}"
SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_HOST = os.getenv("SERVER_HOST")
BACKEND_CORS_ORIGINS = os.getenv(
    "BACKEND_CORS_ORIGINS"
)  # a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000, http://localhost:8080, http://local.dockertoolbox.tiangolo.com"
PROJECT_NAME = os.getenv("PROJECT_NAME")

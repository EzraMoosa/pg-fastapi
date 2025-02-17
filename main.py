from fastapi import FastAPI
import random
import string
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLReponse

# Create FastAPI object
app = FastAPI()


# Mount the static folder for frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")
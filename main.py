from fastapi import FastAPI
import random
import string
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLReponse

# Create FastAPI object
app = FastAPI()


# Mount the static folder for frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Password generation
def generate_password(length: int = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# API route to generate a password
@app.get("/generate")
def get_password(length: int = 12):
    return {"password": generate_password(length)}

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import random
import string
from fastapi.staticfiles import StaticFiles


# Create FastAPI object
app = FastAPI()


# Mount the static & templates folder for frontend files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Password generation
def generate_password(length: int = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# API route to generate a password
@app.get("/generate")
def get_password(length: int = 12):
    return {"password": generate_password(length)}


# Server frontend
@app.get("/")
def serve_frontend(request: Request, length: int = 12):
    password = generate_password(length)
    return templates.TemplateResponse("index.html", {"request": request, "password": password})
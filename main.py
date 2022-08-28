from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


with open('app/form.html', 'r') as f:
    form = f.read()

with open("app/text.html", "r") as t:
    texthi = t.read()

@app.get("/")
async def root():
    return HTMLResponse(form)


@app.get("/tehi")
async def say_hello():
    return HTMLResponse(texthi)

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html = ""
with open('form.html', 'r') as f:
    html = f.read()

@app.get("/")
async def root():
    return HTMLResponse(html)


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

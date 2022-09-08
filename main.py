from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from fastapi.responses import HTMLResponse

import re

nv = re.match("^[A-Za-z]*$","NotValidString123--___")
v = re.match("^[A-Za-z]*$","ValidString")

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


@app.get("/greeting", response_class=HTMLResponse)
async def api_data(request: Request):
    name = request.query_params.get("name")
    if re.match("^[A-Za-z]*$",name):
        return """
           <html>
               <head>
                   <title>Some HTML in here</title>
               </head>
               <body onload="myFunction()">
                   <script>
                        function myFunction() {
                            alert('Его величество """+name + """')
                        }
                    </script>
                   </body>
           </html>
        """
    else:
        return """
           <html>
               <head>
                   <title>Some HTML in here</title>
               </head>
               <body onload="myFunction()">
                   <script>
                        function myFunction() {
                            alert('Имя должно содержать буквы!')
                        }
                    </script>
                   </body>
           </html>
        """
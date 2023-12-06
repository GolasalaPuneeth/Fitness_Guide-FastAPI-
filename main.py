from fastapi import FastAPI ,Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import OpenAI_decorator
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    username: str
    age: str
    weight: str
    height: str
    description: str

    def __repr__(self) -> str:
        return f"{self.username} - {self.age} - {self.weight} - {self.height}"

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")




@app.get("/")
async def welcome(request :Request):
    #data = templates.TemplateResponse("index.html",{"request": request})
    return templates.TemplateResponse("index.html",{"request": request})



@app.post("/users")
async def create_user( request :Request,  username :str = Form(...),age: str = Form(...),  weight: str =Form(...), height: str=Form(...), description: str=Form(...)):
    print(username,age,weight,height, description)
    html = OpenAI_decorator.AI_generater(name=username,age=age,weight=weight,height=height,description=description)
    return HTMLResponse(html)



if __name__=="__main__":
    uvicorn.run(app)
from fastapi import FastAPI ,Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import OpenAI_decorator
from fastapi.responses import HTMLResponse
import TwilioClient


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
    return templates.TemplateResponse("index.html",{"request": request})

@app.get("/signin")
async def signinpage(request :Request):
    return templates.TemplateResponse("signin.html",{"request": request})

@app.post("/signin")
async def signin(request :Request, SignInFirstName :str = Form(...), SignInLastName: str = Form(...),  Email: str =Form(...), country: str=Form(...), number: int =Form(...), Gender: str =Form(...)):
    print(SignInFirstName)
    print(SignInLastName)
    print(Email)
    print(country)
    print(number)
    print(Gender)
    OTP = 1242342 #TwilioClient.sendOTP(number)
    print(OTP)
    return templates.TemplateResponse("OTP.html",{"request": request,"OTP":OTP})

@app.get("/BasicPlan")
async def basicPlan(request :Request):
    return templates.TemplateResponse("login.html",{"request": request})

@app.get("/validator")
async def validator(request :Request, OTP:str = Form(...)):
    return {"status":"scuss"}#templates.TemplateResponse("login.html",{"request": request})


@app.post("/users")
async def create_user( request :Request,  username :str = Form(...),age: str = Form(...),  weight: str =Form(...), height: str=Form(...), description: str=Form(...)):
    print(username,age,weight,height, description)
    html = OpenAI_decorator.AI_generater(name=username,age=age,weight=weight,height=height,description=description)
    return HTMLResponse(html)



if __name__=="__main__":
    uvicorn.run(app)
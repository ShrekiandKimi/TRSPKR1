from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import models

app = FastAPI()

feedbacks: list[models.Feedback] = []

user = models.User(name="Ваше Имя и Фамилия", age=1)

class Numbers(BaseModel):
    num1: float
    num2: float

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.post("/calculate")
async def calculate(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def check_user(user_data: models.User):
    is_adult = user_data.age >= 18
    return {
        "name": user_data.name,
        "age": user_data.age,
        "is_adult": is_adult
    }

@app.post("/feedback")
async def create_feedback(feedback: models.Feedback):
    feedbacks.append(feedback)
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}

@app.get("/feedbacks")
async def get_all_feedbacks():
    return feedbacks
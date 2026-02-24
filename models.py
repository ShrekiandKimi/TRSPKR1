from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    name: str
    age: int

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator('message')
    def validate_message(cls, v: str) -> str:
        forbidden_words = ['кринж', 'рофл', 'вайб']
        v_lower = v.lower()

        for word in forbidden_words:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        
        return v
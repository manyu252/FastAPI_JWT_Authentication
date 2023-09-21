from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Demo Post",
                "content": "Demo Content"
            }
        }


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "user_demo": {
                "name": "Demo User",
                "email": "test@example.com",
                "password": "123"
            }
        }

class LoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "login_demo": {
                "email": "test@example.com",
                "password": "123"
            }
        }

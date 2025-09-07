from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any, List, Literal


class personal_info(BaseModel):

    name : str = Field(...,min_length=3,max_length=20,description="this is name")
    age : int | None = Field(...,ge=0, description="this is age")
    email : str = Field(...,description="this is email")

    # Field validator for email
    @field_validator('email')
    def email_check(cls, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        elif ".com" not in value:
            return value + ".com"
        else:
            return value

pyd_ins = personal_info(**{"name": "Ansh Lamba", "age": 25, "email": "ansh.lamb@aexample"})

print(pyd_ins)
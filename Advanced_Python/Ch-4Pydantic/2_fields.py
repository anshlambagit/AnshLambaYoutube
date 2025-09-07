from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List, Literal


class personal_info(BaseModel):

    name : str = Field(...,min_length=3,max_length=20,description="this is name")
    age : int | None = Field(...,ge=0, description="this is age")
    email : EmailStr = Field(...,description="this is email")
    gender : Literal["male", "female", "other"] = Field(...,description="this is gender")
    salaries : List[int] = Field(...,description="this is salaries")

def main(para1:personal_info):

    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salaries:", para1.salaries)

pyd_ins = personal_info(**{"name": "Ansh Lamba", "age": 25, "email": "anshlamba@example.com", "gender": "male", "salaries": [0,0]})

main(pyd_ins)
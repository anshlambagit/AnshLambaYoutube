from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal 


class addrress(BaseModel):

    street : str = Field(...,description="this is street")
    city : str = Field(...,description="this is city")
    state : str = Field(...,description="this is state")
    country : str = Field(...,description="this is country")
    zip_code : str = Field(...,description="this is zip code")


class personal_info(BaseModel):

    name : str = Field(...,description="this is name")
    age : int = Field(...,description="this is age")
    email : str = Field(...,description="this is email")
    address : addrress = Field(...,description="this is address")


pyud_ins = personal_info(**{
    "name": "Ansh Lamba",
    "age": 30,
    "email": "ansh@example.com",
    "address": addrress(**{
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "country": "USA",
        "zip_code": "12345"
    })
})

print(pyud_ins)
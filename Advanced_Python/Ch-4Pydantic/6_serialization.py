from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal 


class input(BaseModel):

    query : str = Field(...,description="this is query")

class output(BaseModel):

    query : str = Field(...,description="query")
    result : str = Field(...,description="this is result")


def process_data(p_input:input) -> output:

    input_query = p_input.query
    result = "Hello Bro"

    pyd_output = output(**{"query":input_query,"result":result})

    return pyd_output


input_query = input(**{"query":"How are you?"})
response = process_data(input_query)
print(response)

print("-------------------------------")
# Serialization to Dictionary
print(response.model_dump())

print("---------------------------------")
print(response.model_dump_json())
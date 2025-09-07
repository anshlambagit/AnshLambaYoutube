from pydantic import BaseModel, Field, StrictInt


class ansh(BaseModel):

    x : StrictInt = Field(...,description="this is x")
    y : str = Field(default="Ansh Lamba")


pyd_input = ansh(**{"x": 1})

print(pyd_input)

def main(para1:ansh):

    print("Hello Ansh Lamba")


main(pyd_input)
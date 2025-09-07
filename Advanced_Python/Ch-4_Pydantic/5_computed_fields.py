from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal 


class orders(BaseModel):

    id : int = Field(...,description="Order Id")
    units: int = Field(..., description="Units")
    amount : int = Field(...,description="Amount Per Unit")

    @computed_field
    @property
    def total_amount(self)-> int:
        return self.units*self.amount
    
pyd_ins = orders(**{"id":1,"units":10,"amount":100})
print(pyd_ins)
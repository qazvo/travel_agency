from pydantic import BaseModel
from datetime import datetime
from typing import Optional 

class customers(BaseModel):
    id: int
    FIO: str
    number_phone: str

class managers(BaseModel):
    id: int
    FIO: str
    number_phone: str
    passport: str

class applications(BaseModel):
    id: int
    desired_travel: str
    customer_id: int
    manager_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    status: Optional[bool] = False

class implementers(BaseModel):
    id: int
    name: int
    description: str
    contact_detail: str

class contracts(BaseModel):
    id: int
    application_id: int
    implementer_id: int
    comment_imp: str

class posts(BaseModel):
    id: int
    name: str 
    authority: str

class users(BaseModel):
    id: int
    login: str
    password: str
    post_id: int
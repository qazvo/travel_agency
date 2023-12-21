import fastapi

from database.models_db import customers
from resolvers import res_customers

customers_router = fastapi.APIRouter(prefix= "/customers", tags= ["Customers"])

@customers_router.get(path= "/get/one", response_model= dict)
def get_customer(customer_id: int) -> dict:
    return res_customers.get_customer(customer_id= customer_id)

@customers_router.get(path= "/get/all", response_model= dict)
def get_customers() -> dict:
    return res_customers.get_customers()

@customers_router.post(path= "/add", response_model= dict)
def add_customer(customer: customers) -> dict:
    return res_customers.add_customer(customer= customer)

@customers_router.put(path="/update/number_phone", response_model= dict)
def update_number_phone(customer: customers) -> dict:
    return res_customers.update_number_phone(customer= customer)

@customers_router.delete(path= "/delete", response_model= dict)
def delete_customer(customer_id : int) -> dict:
    return res_customers.delete_customer(customer_id= customer_id)
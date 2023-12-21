import fastapi

from database.models_db import contracts
from resolvers import res_contracts

contracts_router = fastapi.APIRouter(prefix= "/contracts", tags= ["Contracts"])

@contracts_router.get(path="/get/one", response_model= dict)
def get_contract(contract_id: int) -> dict:
    return res_contracts.get_contract(contract_id= contract_id)

@contracts_router.get(path="/get/all", response_model= dict)
def get_contracts() -> dict:
    return res_contracts.get_contracts()

@contracts_router.post(path="/add", response_model= dict)
def add_contract(contract: contracts) -> dict:
    return res_contracts.add_contract(contract= contract)

@contracts_router.put(path="/update/implementer", response_model= dict)
def update_implementer(contract: contracts) -> dict:
    return res_contracts.update_implementer(contract= contract)

@contracts_router.put(path="/update/comment", response_model= dict)
def update_comment(contract: contracts) -> dict:
    return res_contracts.update_comment(contract= contract)

@contracts_router.delete(path="/delete", response_model= dict)
def delete_contract(contract_id : int) -> dict:
    return res_contracts.delete_contract(contract_id= contract_id)
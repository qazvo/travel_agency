from database.db_manager import db_manager

from database.models_db import contracts

def get_contract(contract_id: int) -> dict:
    return db_manager.execute(query= """SELECT * FROM contracts WHERE id = ?""",
                              args= (contract_id,))

def get_contracts() -> dict:
    return db_manager.execute(query= """SELECT * FROM contracts""", many= True)

def add_contract(contract: contracts) -> dict:
    return db_manager.execute(query= """INSERT INTO contracts(application_id, implementer_id, comment_imp)
                                        VALUES(?, ?, ?)""",
                              args= (contract.application_id, contract.implementer_id, contract.comment_imp))

def update_implementer(contract: contracts) -> dict:
    return db_manager.execute(query= """UPDATE contracts SET implementer_id = ? WHERE id = ?""",
                              args= (contract.implementer_id, contract.id))

def update_comment(contract: contracts) -> dict:
    return db_manager.execute(query= """UPDATE contracts SET comment_imp = ? WHERE id = ?""",
                              args= (contract.comment_imp, contract.id))

def delete_contract(contract_id: int) -> dict:
    return db_manager.execute(query= """DELETE FROM contracts WHERE id = ?""",
                              args= (contract_id,))


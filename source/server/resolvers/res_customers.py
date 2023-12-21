from database.db_manager import db_manager

from database.models_db import customers

def get_customer(customer_id: int) -> dict:
    return db_manager.execute(query= """SELECT * FROM customers WHERE id = ?""",
                              args= (customer_id,))

def get_customers() -> dict:
    return db_manager.execute(query= """SELECT * FROM customers""", many= True)

def add_customer(customer: customers) -> dict:
    return db_manager.execute(query= """INSERT INTO customers(FIO, number_phone) VALUES (?, ?)""",
                              args= (customer.FIO, customer.number_phone))

def update_number_phone(customer: customers) -> dict:
    return db_manager.execute(query= """UPDATE customers SET number_phone = ? WHERE id = ?""",
                              args= (customer.number_phone, customer.id))

def delete_customer(customer_id: int) -> dict:
    return db_manager.execute(query="""DELETE FROM customers WHERE id = ?""",
                              args= (customer_id,))


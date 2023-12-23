from database.db_manager import db_manager

from database.models_db import users

def get_user(user_id: int) -> dict:
    return db_manager.execute(query= """SELECT * FROM users WHERE id = ?""",
                              args= (user_id,))

def get_users() -> dict:
    return db_manager.execute(query= """SELECT * FROM users""", many= True)

def check_user(user: users) -> users:
    return db_manager.execute(query= """SELECT id, post_id FROM users WHERE login = ? AND password = ?""",
                              args= (user.login, user.password))

def add_user(user: users) -> dict:
    return db_manager.execute(query= """INSERT INTO users(login, password, post_id)
                                        VALUES(?,?,?)""",
                              args= (user.login, user.password, user.post_id))

def update_password(user: users) -> dict:
    return db_manager.execute(query= """UPDATE users SET passsword = ? WHERE id = ?""",
                              args= (user.password, user.id))

def delete_user(user_id: int) -> dict:
    return db_manager.execute(query= """DELETE FROM users WHERE id = ?""",
                              args= (user_id,))


import fastapi

from database.models_db import users
from resolvers import res_users

users_router = fastapi.APIRouter(prefix= "/users", tags= ["Users"])

@users_router.get(path="/get/one", response_model= dict)
def get_user(user_id: int) -> dict:
    return res_users.get_user(user_id= user_id)

@users_router.get(path="/get/all", response_model= dict)
def get_users() -> dict:
    return res_users.get_users()

@users_router.get(path="/get/check", response_model= dict)
def check_users(user: users) -> users:
    return res_users.check_user(user= user)

@users_router.post(path="/add", response_model= dict)
def add_user(user: users) -> dict:
    return res_users.add_user(user= user)

@users_router.put(path="/update/password", response_model= dict)
def update_password(user: users) -> dict:
    return res_users.update_password(user= user)

@users_router.delete(path="/delete/{user_id}", response_model= dict)
def delete_user(user_id: int) -> dict:
    return res_users.delete_user(user_id= user_id)
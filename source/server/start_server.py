from database.db_manager import db_manager
from settings import HOST, PORT
import uvicorn
from fastapi import FastAPI
from routers import applications, customers, contracts, users
from fastapi.responses import RedirectResponse

app = FastAPI(title="travel_agency")

app.include_router(applications.applications_router)
app.include_router(customers.customers_router)
app.include_router(contracts.contracts_router)
app.include_router(users.users_router)

@app.router.get('/')
def start_page() -> RedirectResponse:
    return RedirectResponse('/docs')

if __name__ == "__main__":
    uvicorn.run(app='start_server:app', reload = True, host = HOST, port = PORT)
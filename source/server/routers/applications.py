import fastapi

from database.models_db import applications
from resolvers import res_applications

applications_router = fastapi.APIRouter(prefix= "/applications", tags= ["Applications"])

@applications_router.get(path= "/get/one", response_model= dict)
def get_application(application_id: int) -> dict:
    return res_applications.get_application(application_id = application_id)

@applications_router.get(path= "/get/all", response_model= dict)
def get_applications() -> dict:
    return res_applications.get_applications()

@applications_router.get(path= "/get/CountCompletedApplications", response_model= dict)
def get_count_completed_applications() -> dict:
    return res_applications.get_count_completed_applications()

@applications_router.get(path= "/get/MidleTimeCompletedApplications", response_model= dict)
def get_midle_time_completed_applications() -> dict:
    return res_applications.get_midle_time_completed_applications()

@applications_router.get(path= "/get/StatisticTravels", response_model= dict)
def get_statistic_travels() -> dict:
    return res_applications.get_statistic_travels()

@applications_router.post(path= "/add", response_model= dict)
def add_application(application: applications) -> dict:
    return res_applications.add_application(application= application)

@applications_router.put(path= "/update/manager", response_model= dict)
def update_manager(application: applications) -> dict:
    return res_applications.update_manager(application= application)

@applications_router.put(path= "/update/status", response_model= dict)
def update_status(application: applications) -> dict:
    return res_applications.update_status(application= application)

@applications_router.put(path= "/update/desired_travel", response_model= dict)
def update_desired_travel(application: applications) -> dict:
    return res_applications.update_desired_travel(application= application)

@applications_router.delete(path= "/delete", response_model= dict)
def delete_application(application_id: int) -> dict:
    return res_applications.delete_application(application_id= application_id)

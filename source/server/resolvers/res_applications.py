from database.db_manager import db_manager

from database.models_db import applications

def get_application(application_id: int) -> dict:
    return db_manager.execute(query= """SELECT * FROM applications WHERE id = ?""",
                              args= (application_id,))

def get_applications() -> dict:
    return db_manager.execute(query= """SELECT * FROM applications""", many= True)

def get_count_completed_applications() -> dict:
    return db_manager.execute(query= """SELECT COUNT(id) FROM applications WHERE status = true""")

def get_midle_time_completed_applications() -> dict:
    return db_manager.execute(query= """SELECT CAST(AVG(julianday(end_date) - julianday(start_date))*24 as INT) FROM applications WHERE status = 1""")

def get_statistic_travels() -> dict:
    return db_manager.execute(query= """SELECT desired_travel, COUNT(id) 
                                        FROM applications GROUP BY desired_travel""", many= True)

def add_application(application: applications) -> dict:
    return db_manager.execute(query= """INSERT INTO applications(desired_travel, customer_id, manager_id, start_date, status)
                                        VALUES(?, ?, ?, ?, ?)""",
                              args= (application.desired_travel, application.customer_id, application.manager_id, application.start_date, application.status))

def update_status(application: applications) -> dict:
    return db_manager.execute(query= """UPDATE applications SET status = ? WHERE id = ?""",
                              args= (application.status, application.id))

def update_manager(application: applications) -> dict:
    return db_manager.execute(query= """UPDATE applications SET manager_id = ? WHERE id = ?""",
                              args= (application.manager_id, application.id))

def update_desired_travel(application: applications) -> dict:
    return db_manager.execute(query= """UPDATE applications SET desired_travel = ? WHERE id = ?""",
                              args= (application.desired_travel, application.id))

def delete_application(application_id: int) -> dict:
    return db_manager.execute(query= """DELETE FROM applications WHERE id = ?""",
                              args= (application_id,))

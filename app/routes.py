from fastapi import APIRouter
from dal import *
router = APIRouter(prefix="/employees",tags=["Employees"])


@router.get("/q1")
def get_engineering_high_salary_employees():
    return get_engineering_high_salary_employees()

@router.get("/q2")
def get_employees_by_age_and_role():
    return get_employees_by_age_and_role()

@router.get("/q3")
def get_top_seniority_employees_excluding_hr():
    return get_top_seniority_employees_excluding_hr()

@router.get("/q4")
def get_employees_by_age_or_seniority():
    return get_employees_by_age_or_seniority()

@router.get("/q5")
def get_managers_excluding_departments():
    return get_managers_excluding_departments()

@router.get("/q6")
def get_employees_by_lastname_and_age():
    return get_employees_by_lastname_and_age()

 






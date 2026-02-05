from pymongo import MongoClient
from connection import get_connection
 


def get_engineering_high_salary_employees():
     
    collection = get_connection() 
    employees = collection.find({'job_role.department': 'Engineering', 'salary': {'$gt': 65000}}, {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0})
    client.close()
    return employees

def get_employees_by_age_and_role():
    collection = get_connection() 
    employees = collection.find({'$or': [{'job_role.title': 'Engineer'},{'job_role.title': 'Specialist'}], 'age': {'$gte': 30, '$lte': 45}}, {'_id': 0})
    client.close()
    return employees


def get_top_seniority_employees_excluding_hr():
    collection = get_connection() 
    employees = collection.find({'job_role.department': {'$ne': 'HR'}}).sort('years_at_company', -1 ).limit(7)
    client.close()
    return employees

def get_employees_by_age_or_seniority():
    collection = get_connection() 
    q = {"$or":[{"age":{'$gte': 50}}, {"years_at_company":{'$lte':3}}]}
    p = {'employee_id': 1, 'name': 1, 'age': 1, '_id': 0, "years_at_company":1}
    employees = collection.find(q,p)
    client.close()
    return employees

def get_managers_excluding_departments():
    collection = get_connection() 
    q ={'job_role.title': 'Manager', 'job_role.department': {'$nin':['Sales', 'Marketing']}}
    p = {}
    employees = collection.find(q, p)
    client.close()
    return employees

def get_employees_by_lastname_and_age():
    collection = get_connection() 
    q ={'age': {'$lt': 35}, 'name': {'$regex':' Wright$'},'name':{'$regex':' Nelson$'}}
    p =  {'name': 1, 'age': 1, 'job_role.department': 1, '_id': 0}
    employees = collection.find(q, p)
    client.close()
    return employees



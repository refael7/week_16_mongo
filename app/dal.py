from pymongo import MongoClient

def get_client():
    client = MongoClient('mongodb://localhost:27017')
    return client


def get_engineering_high_salary_employees():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    employees = collection.find({'job_role.department': 'Engineering', 'salary': {'$gt': 65000}}, {'employee_id': 1, 'name': 1, 'salary': 1, '_id': 0})
    client.close()
    return employees

def get_employees_by_age_and_role():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    employees = collection.find({'$or': [{'job_role.title': 'Engineer'},{'job_role.title': 'Specialist'}], 'age': {'$gte': 30, '$lte': 45}}, {'_id': 0})
    client.close()
    return employees


def get_top_seniority_employees_excluding_hr():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    employees = collection.find({'job_role.department': {'$ne': 'HR'}}).sort('years_at_company', -1 ).limit(7)
    client.close()
    return employees

def get_employees_by_age_or_seniority():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    q = {"$or":[{"age":{'$gte': 50}}, {"years_at_company":{'$lte':3}}]}
    p = {'employee_id': 1, 'name': 1, 'age': 1, '_id': 0, "years_at_company":1}
    employees = collection.find(q,p)
    client.close()
    return employees

def get_managers_excluding_departments():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    q ={'job_role.title': 'Manager', 'job_role.department': {'$nin':['Sales', 'Marketing']}}
    p = {}
    employees = collection.find(q, p)
    client.close()
    return employees

def get_employees_by_lastname_and_age():
    client = get_client()
    db = client['ecomerce_db']
    collection = db['employee_data_advanced']
    q ={'age': {'$lt': 35}, 'name': {'$regex':' Wright$'},'name':{'$regex':' Nelson$'}}
    p =  {'name': 1, 'age': 1, 'job_role.department': 1, '_id': 0}
    employees = collection.find(q, p)
    client.close()
    return employees



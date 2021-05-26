from flask import Blueprint
from sqlalchemy import func
from src.api.utils import responses as resp
from src.api.models.employees import Employee, EmployeeSchema

reports_route = Blueprint("reports_route", __name__)


def get_query_older():
    return Employee.query.filter(
        Employee.birth_date == func.min(Employee.birth_date).select()
    ).scalar()


def get_query_younger():
    return Employee.query.filter(
        Employee.birth_date == func.max(Employee.birth_date).select()
    ).scalar()


@reports_route.route('/employees/age', methods=['GET'])
def get_age():
    employee_schema = EmployeeSchema()
    older = employee_schema.dump(get_query_older())
    younger = employee_schema.dump(get_query_younger())
    return resp.response_with(resp.SUCCESS_200, value={'younger': younger, 'older': older})


def get_lowest_salary():
    return Employee.query.filter(
        Employee.salary == func.min(Employee.salary).select()
    ).scalar()


def get_highest_salary():
    return Employee.query.filter(
        Employee.salary == func.max(Employee.salary).select()
    ).scalar()


@reports_route.route('/employees/salary', methods=['GET'])
def get_salary_gap():
    employee_schema = EmployeeSchema()
    lowest = employee_schema.dump(get_lowest_salary())
    highest = employee_schema.dump(get_highest_salary())
    return resp.response_with(resp.SUCCESS_200, value={'lowest': lowest, 'highest': highest})

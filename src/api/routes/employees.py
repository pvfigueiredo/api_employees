from flask import Blueprint, request
from src.api.utils.responses import response_with
from src.api.utils import responses as resp
from src.api.models.employees import Employee, EmployeeSchema
from src.api.utils.database import db

employee_routes = Blueprint("employee_routes", __name__)


@employee_routes.route('/', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        employee_schema = EmployeeSchema()
        employee = employee_schema.load(data)
        result = employee_schema.dump(employee.create())
        return response_with(resp.SUCCESS_201, value={"employee": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@employee_routes.route('/', methods=['GET'])
def get_employees():
    fetched = Employee.query.all()
    employee_schema = EmployeeSchema(many=True)
    employees = employee_schema.dump(fetched)
    response = response_with(resp.SUCCESS_200, value={"employee": employees})
    return response


@employee_routes.route('/<int:id_employee>', methods=['GET'])
def get_employee(id_employee):
    fetched = Employee.query.get_or_404(id_employee)
    employee_schema = EmployeeSchema()
    employees = employee_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={'employee': employees})


@employee_routes.route('/<int:id_employee>', methods=['PUT'])
def update_employee(id_employee):
    data = request.get_json()
    emp = Employee.query.get_or_404(id_employee)
    emp.name = data['name']
    emp.email = data['email']
    emp.salary = data['salary']
    emp.department = data['department']
    emp.birth_date = data['birth_date']
    db.session.add(emp)
    db.session.commit()
    employee_schema = EmployeeSchema()
    employee = employee_schema.dump(emp)
    return response_with(resp.SUCCESS_200, value={'employee': employee})


@employee_routes.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee_to_del = Employee.query.get_or_404(employee_id)
    db.session.delete(employee_to_del)
    db.session.commit()
    return response_with(resp.SUCCESS_204)

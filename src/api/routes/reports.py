from flask import Blueprint, request
from src.api.utils.responses import response_with
from src.api.utils import responses as resp
from src.api.models.employees import Employee, EmployeeSchema
from src.api.utils.database import db

reports_route = Blueprint("reports_route", __name__)

@reports_route.route('/emplyees/age', methods=['GET'])
def age():

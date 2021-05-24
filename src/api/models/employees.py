from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.Email(100))
    department = db.Column(db.String(50))
    salary = db.Column(db.Double)
    birth_day = db.Column(db.DateTime)

    def __init__(self, name: str, email: str, department: str, salary: float, birth_day: str):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.birth_day = birth_day


class EmployeeSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Employee
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    department = fields.String(required=True)
    salary = fields.Float(required=True)
    birth_day = fields.Date(required=True)
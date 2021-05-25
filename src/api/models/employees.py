from src.api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields


class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    department = db.Column(db.String(50))
    salary = db.Column(db.Float)
    birth_date = db.Column(db.String(10))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, email, department, salary, birth_date):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.birth_date = birth_date

    def __repr__(self):
        return f'{self.id}'

class EmployeeSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Employee
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    email = fields.String(required=True)
    department = fields.String(required=True)
    salary = fields.Float(required=True)
    birth_date = fields.String(required=True)

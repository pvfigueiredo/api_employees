import os

from flask import Flask, logging
from src.api.utils.database import db
import src.api.utils.responses as resp
from src.api.config.config import *
from src.api.routes import employees
from src.api.utils.responses import response_with

app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(employees.employee_routes, url_prefix='/employees')


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request(e):
    logging.error(e)
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found(e):
    logging.error(e)
    return response_with(resp.SERVER_ERROR_404)

db.init_app(app)
with app.app_context():
    db.create_all()

#
# @app.route('/employees', methods=['POST', 'GET'])
# def employees():
#     if request.method == 'POST':
#         input_json = request.get_json(force=True)
#         dict_to_return = {'text': input_json}
#         return jsonify(dict_to_return)
#     else:
#         return jsonify(response)
#
#
# @app.route('/employees/<int:id>', methods=['PUT', 'DELETE', 'GET'])
# def employees_id(employee_id: int):
#     if request.method == 'PUT':
#         input_json = request.get_json(force=True)
#         dict_to_return = {'text': input_json}
#         return jsonify(dict_to_return)
#     elif request.method == 'DELETE':
#         return {"id": employee_id, "status": 200}
#     else:
#         return jsonify(response[employee_id - 1])
#
#
# @app.route('/reports/employees/salary', methods=['GET'])
# def get_salaries():
#     result = {}
#     if request.method == 'GET':
#         result['lowest'] = get_lowest_salary()
#         result['highest'] = get_highest_salary()
#         return jsonify(result)
#
#
# @app.route('/reports/employees/age', methods=['GET'])
# def get_ages():
#     result = {}
#     if request.method == 'GET':
#         result['younger'] = get_younger()
#         result['older'] = get_older()
#         return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', use_reloader=False)

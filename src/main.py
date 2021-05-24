import os
from flask import Flask, request
from flask import jsonify
from api.config.config import *
from api.reposta_test import response, get_lowest_salary, get_highest_salary, get_younger, get_older

app = Flask(__name__)

if os.environ.get('WORK_ENV') == 'PROD':
    app_config = ProductionConfig
elif os.environ.get('WORK_ENV') == 'TEST':
    app_config = TestingConfig
else:
    app_config = DevelopmentConfig

app.config.from_object(app_config)


# db.init_app(app)
# with app.app_context():
#     db.create_all()


@app.route('/employees', methods=['POST', 'GET'])
def employees():
    if request.method == 'POST':
        input_json = request.get_json(force=True)
        dict_to_return = {'text': input_json}
        return jsonify(dict_to_return)
    else:
        return jsonify(response)


@app.route('/employees/<int:id>', methods=['PUT', 'DELETE', 'GET'])
def employees_id(employee_id: int):
    if request.method == 'PUT':
        input_json = request.get_json(force=True)
        dict_to_return = {'text': input_json}
        return jsonify(dict_to_return)
    elif request.method == 'DELETE':
        return {"id": employee_id, "status": 200}
    else:
        return jsonify(response[employee_id - 1])


@app.route('/reports/employees/salary', methods=['GET'])
def get_salaries():
    result = {}
    if request.method == 'GET':
        result['lowest'] = get_lowest_salary()
        result['highest'] = get_highest_salary()
        return jsonify(result)


@app.route('/reports/employees/age', methods=['GET'])
def get_ages():
    result = {}
    if request.method == 'GET':
        result['younger'] = get_younger()
        result['older'] = get_older()
        return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', use_reloader=False)

import os

from flask import Flask
from src.api.utils.database import db
import src.api.utils.responses as resp
from src.api.config.config import *
from src.api.routes import employees, reports
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
app.register_blueprint(reports.reports_route, url_prefix='/reports')


@app.after_request
def add_header(response):
    return response


@app.errorhandler(400)
def bad_request():
    return response_with(resp.BAD_REQUEST_400)


@app.errorhandler(500)
def server_error():
    return response_with(resp.SERVER_ERROR_500)


@app.errorhandler(404)
def not_found():
    return response_with(resp.SERVER_ERROR_404)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', use_reloader=False)

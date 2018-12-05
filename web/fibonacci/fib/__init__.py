from flask import Blueprint

from fibonacci.fib.log_request import log_request

fib = Blueprint('fib', __name__)
fib.before_app_request(log_request)

from . import views
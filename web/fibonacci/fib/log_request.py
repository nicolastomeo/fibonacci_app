from flask import request

from fibonacci import db
from fibonacci.models import Request


def log_request():
    """
    Function that stores /fib requests in the database

    """
    if request.path.startswith('/fib'):
        req = Request(url=request.url)
        db.session.add(req)
        db.session.commit()

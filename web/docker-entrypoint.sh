#!/bin/bash
flask db upgrade
gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name fibo -b 0.0.0.0:8000 --reload run:app

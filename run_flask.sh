#!/bin/bash
source .venv/bin/activate
export FLASK_APP=flaskapp/consumerapi.py
export FLASK_ENV=development
flask run


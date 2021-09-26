#!/bin/bash

export FLASK_APP=app.py
export FLASK_RUN_PORT=4000
export FLASK_ENV=development

python3 app.py

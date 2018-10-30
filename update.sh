#!/bin/bash
set -e
pip install -r requirements.txt
python manage.py migrate
yarn install --non-interactive
yarn build

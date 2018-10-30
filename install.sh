#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@localhost', 'admin')" | python manage.py shell
yarn
yarn build

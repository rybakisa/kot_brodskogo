#!/bin/bash
set -e
export $(egrep -v '^#' .env | xargs)

start() {
    nohup python manage.py runserver localhost:${SERVER_PORT} > ./dev-server.log 2>&1 &
    echo "development web server started at http://localhost:${SERVER_PORT}"
    echo "log: dev-server.log"
    exit 0
}

stop() {
    kill $(lsof -t -i:${SERVER_PORT})
    echo "development web server on port ${SERVER_PORT} is stopped"
    exit 0
}

error_option() {
    echo "unknown option \"$1\"
known options:

start
stop

if no option, \"start\" will be used"
    exit 1
}

if [[ "$@" = *"stop"* ]]; then
    stop
elif [[ "$@" = *"start"* ]]; then
    start
elif [[ "$@" = "" ]]; then
    start
else
    error_option $@
fi


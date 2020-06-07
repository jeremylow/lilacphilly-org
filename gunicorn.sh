#!/bin/bash

NAME="lilacphilly.org"
SERVERDIR=/opt/lilacphilly_org
VENVDIR=/opt/lilacphilly_org/venv
USER=www-data
GROUP=www-data
PORT=8001
NUM_WORKERS=2

cd $SERVERDIR
source $VENVDIR/bin/activate

DJANGO_WSGI_MODULE=config.wsgi
export PYTHONPATH=$SERVERDIR:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=config.settings.production


exec $VENVDIR/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=info \
    --bind=127.0.0.1:$PORT


#!/bin/bash
source /home/givitoome/givitoo/Backend/venv/bin/activate
export DJANGO_SETTINGS_MODULE=givito.settings
cd /home/givitoome/givitoo/Backend
exec /home/givitoome/givitoo/Backend/venv/bin/gunicorn givito.wsgi:application \
--bind localhost:8000 \
--workers 4 \
--user=givitoome

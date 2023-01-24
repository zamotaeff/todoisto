#!/bin/bash
ls -lah
cd ./backend
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python manage.py migrate
fi
cd ..
exec "$@"
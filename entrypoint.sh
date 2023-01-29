#!/bin/bash
ls -lah
# shellcheck disable=SC2164
cd ./backend
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python manage.py migrate
fi
# shellcheck disable=SC2103
cd ..
exec "$@"

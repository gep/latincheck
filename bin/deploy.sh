#!/bin/sh

# terminate uwsgi emperror process
kill -15 `ps -ef | grep 'uwsgi --emperor' | grep -v grep | awk '{print $2}'`

uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/projects/lifeline-latincheck/logs/uwsgi/uwsgi-emperor.log

# generate assets
cd /var/projects/lifeline-latincheck
python manage.py collectstatic --noinput
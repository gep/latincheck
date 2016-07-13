#!/bin/sh

# terminate uwsgi emperror process
echo "Terminating uwsgi emperor..."
kill -15 `ps -ef | grep 'uwsgi --emperor' | grep -v grep | awk '{print $2}'`

echo "Launching uwsgi emperor..."
uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/logs/uwsgi/uwsgi-emperor.log

# generate assets
echo "Generating assets..."
cd /var/projects/lifeline-latincheck
python manage.py collectstatic --noinput

echo "Compiling translations..."
python manage.py compilemessages
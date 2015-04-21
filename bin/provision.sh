#!/bin/sh

if [ `whoami` != "root" ]; then
	echo "You must be root to provision this";
	exit;
fi

apt-get update
apt-get install -y python-pip
apt-get install -y python2.7-dev
pip install Django==1.8
apt-get -y install nginx
pip install uwsgi
mkdir /etc/uwsgi
mkdir /etc/uwsgi/vassals
ln -s /var/projects/lifeline-latincheck/config/uwsgi/uwsgi.ini /etc/uwsgi/vassals/
touch /var/projects/lifeline-latincheck/logs/uwsgi/latincheck.log
chmod -R 777 /var/projects/lifeline-latincheck/logs/uwsgi/latincheck.log
# uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data
ln -s /var/projects/lifeline-latincheck/config/nginx/lifeline-latincheck /etc/nginx/sites-enabled/


cd /var/projects/lifeline-latincheck
python manage.py collectstatic --noinput
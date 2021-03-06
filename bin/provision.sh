#!/bin/sh

if [ `whoami` != "root" ]; then
	echo "You must be root to provision this";
	exit;
fi

apt-get update
apt-get install -y python-pip
apt-get install -y python2.7-dev
pip install Django==1.8
apt-get -y install gettext
apt-get -y install nginx
pip install uwsgi
mkdir /etc/uwsgi
mkdir /etc/uwsgi/vassals
ln -s /var/projects/lifeline-latincheck/config/uwsgi/uwsgi.ini /etc/uwsgi/vassals/
touch /var/projects/lifeline-latincheck/logs/uwsgi/latincheck.log
chmod -R 777 /var/projects/lifeline-latincheck/logs/uwsgi/latincheck.log
mkdir /var/log/uwsgi
touch /var/log/uwsgi/uwsgi-emperor.log
chmod -R 777 /var/log/uwsgi/uwsgi-emperor.log
ln -s /var/projects/lifeline-latincheck/config/nginx/lifeline-latincheck /etc/nginx/sites-enabled/

/var/projects/lifeline-latincheck/bin/deploy.sh

#!/bin/sh

if [ `whoami` != "root" ]; then
	echo "You must be root to provision this";
	exit;
fi

apt-get update
apt-get install -y python-pip
pip install Django==1.8
apt-get install -y postgresql
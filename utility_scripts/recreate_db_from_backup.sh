#!/usr/bin/env bash
set -eo pipefail

db_dump=$1

if [ ! "$(whoami)" = "vagrant" ]; then
    echo "This script is meant only for vagrant environment"
    exit 1
fi

if [ -z "$db_dump" ]; then
    echo "Usage: $0 <db_dump_file_path>"
    exit 2
fi

sudo /etc/init.d/supervisor stop

sudo -u  postgres sh -s <<SCRIPT
dropdb pari
createdb pari --owner pari
psql -d pari -c "CREATE EXTENSION postgis;"
PGPASSWORD=pari  psql -U pari -h localhost < "$db_dump"
SCRIPT

cd /vagrant && . pari_env/bin/activate
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('pari', 'admin', 'pari')" | python manage.py shell

sudo /etc/init.d/supervisor start
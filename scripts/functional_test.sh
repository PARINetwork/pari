#!/bin/bash

DATABASE_NAME="test_pari"
DATABASE_USER="pari"
DATABASE_PASSWORD="pari"

echo "Setting up DB"
sudo -u postgres sh -s <<SCRIPT
dropdb $DATABASE_NAME
createdb $DATABASE_NAME --owner $DATABASE_USER
psql -d $DATABASE_NAME -c "CREATE EXTENSION postgis;"
SCRIPT

mkdir -p "media/uploads/"
cp "core/static/img/stories-1.jpg" "media/uploads/stories-1.jpg"

cd /vagrant && . pari_env/bin/activate
python manage.py migrate --settings=pari.settings.test

echo "Starting Server..........."
python manage.py runserver --settings=pari.settings.test > /dev/null 2>&1 &

expected_response=200
end=$((SECONDS+60))
while [ "$SECONDS" -lt "$end" ];
do
  sleep 2
  response=`curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/pages/donate/`
  echo "Waiting for service to start...."
  if [ "$response" == "$expected_response" ]
  then
    is_service_started='true'
    break
  fi
done
if [ "$is_service_started" != 'true' ];
then
   echo "Unable to start the service :("
   exit 1
fi

echo "Starting xvfb"
export DISPLAY=:99
Xvfb -ac :99 > /dev/null 2>&1 &

echo "Running test"
python manage.py test --settings=pari.settings.test --with-coverage --keepdb

echo "Stop service"
pid=$(lsof -i:8000 -t); kill -TERM $pid || kill -KILL $pid

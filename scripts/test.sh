#!/bin/bash

echo "Running Migrations...."
python manage.py migrate --settings=pari.settings.test

echo "Running Collectstatic...."
python manage.py collectstatic --noinput

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
    echo "Service Started........."
    break
  fi
done
if [ "$is_service_started" != 'true' ];
then
   echo "Unable to start the service........"
   exit 1
fi

echo "Running test......."
python manage.py test --settings=pari.settings.test -k -v 3
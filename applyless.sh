python manage.py collectstatic --noinput &&
python manage.py compress --force &&
sudo supervisorctl restart pari:gunicorn_pari &&
sudo service nginx restart
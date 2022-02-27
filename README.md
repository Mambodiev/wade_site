TO RUN THIS PROJECT

source env/bin/activate
python3 manage.py runserver

Connect to admin
wade
9081

python3 manage.py runserver --settings ouest.settings.dev
heroku logs --tail
python manage.py collectstatic
git add .
git commit -a -m 'touch 404 pages'
git push -u origin master
git push heroku master
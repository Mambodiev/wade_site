TO RUN THIS PROJECT
<!--  False -->
source env/bin/activate
python3 manage.py runserver

Connect to admin
wade
9081

python3 manage.py runserver --settings ouest.settings.dev
heroku logs --tail
python manage.py collectstatic

git add .
git commit -m "touch authentication"
git push -u origin master

git push heroku master
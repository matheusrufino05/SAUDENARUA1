grupo: matheus rufino e joao carlos

rodar server

python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

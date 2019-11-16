# DATOS


Datos is a simple CMDB that can be used to store infrastructure reference data.  

Technology Stack 
- Flask-RestPlus
- SQLAlchemy 
- Postgres


## MAC INSTALLATION INSTRUCTIONS
### Postgres installation
```
brew install postgresql  

pg_ctl -D /usr/local/var/postgres start

createdb datos

psql -d datos
```

###  Application setup
git clone https://github.com/osumano/datos.git
(create a virtualenv - best practice)
```
pip install -r requirements.txt

python db_init.py

export PYTHONPATH='.:../'

FLASK_APP=app.py

FLASK_ENV=development

flask run
```

# Datos


## Mac Installation instructions

brew install postgresql  

pg_ctl -D /usr/local/var/postgres start

createdb datos

psql -d datos


## Datos setup
git clone https://github.com/osumano/datos.git
(create a virtualenv - best practice)

pip install -r requirements.txt

python db_init.py


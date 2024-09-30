# prototype-site-e-commerce


python3 -m venv .venv

source .venv/bin/activate

pip install django

python -m django --version

django-admin startproject nom_de_votre_projet .

python manage.py startapp nom_de_votre_app

ajouter la nouvelle app dans INSTALLED_APPS dans le fichier settings.py du projet
# prototype-site-e-commerce

creer environnement virtuel
python3 -m venv .venv

activer environnement virtuel
source .venv/bin/activate

installer django
pip install django

check version et install django
python -m django --version

creer projet
django-admin startproject nom_de_votre_projet .

creer app
python manage.py startapp nom_de_votre_app

dire que l'app fait partie du projet
ajouter la nouvelle app dans INSTALLED_APPS dans le fichier settings.py du projet

install Pillow
install autre trucs 
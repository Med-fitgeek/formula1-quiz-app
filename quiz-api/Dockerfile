# Image de l'API basée sur une image python
FROM python:3.9-alpine

# Création et positionnement du répertoire par défaut dans le container
WORKDIR /app

# Copie du fichier requirements local (machine hôte) vers le container 
# (répertoire /app, car il s'agit du WORKDIR)
COPY requirements.txt requirements.txt

# Copier la base de données SQLite préchargée
COPY quiz.db /app/quiz.db

# Installation des dépendances dans le container
RUN pip install -r requirements.txt

# Variables d'environement de production
ENV FLASK_DEBUG=0
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

# Copie de l'ensemble du code + dépendances
COPY . .

# Informations sur l'image
LABEL maintainer="Nom Prénom <nom.prénom@esiee.fr>" \
    version="1.0"

# Commande de démarrage du serveur gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()", "--log-level", "info", "--error-logfile", "-", "--access-logfile", "-"]
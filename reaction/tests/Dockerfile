# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier de dépendances dans le conteneur
COPY tests/requirements.txt .

# Mettre à jour pip et installer les dépendances avec un délai d'attente augmenté
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copier les répertoires nécessaires dans le conteneur
COPY src/ ./src
COPY tests/ ./tests

# Définir la commande par défaut pour exécuter les tests
CMD ["pytest", "tests/"]

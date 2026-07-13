# Utilisation d'une image de base Python
FROM python:3.10-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Évite les invites interactives bloquantes lors de l'installation apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Installation des dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-fra \
    libtesseract-dev \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    ghostscript \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers de configuration des dépendances
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du code source
COPY . .

# Création des répertoires qui seront montés en volume (pour éviter les erreurs de permission)
RUN mkdir -p /app/TestExtraction/qdrant_data /app/Log /app/RAC/Data /app/data /app/PDF2

# Exposition du port sur lequel FastAPI va tourner
EXPOSE 8600

# Commande de démarrage de l'API avec uvicorn
CMD ["uvicorn", "Interface.fastapi_rag_wrapper:app", "--host", "0.0.0.0", "--port", "8600"]

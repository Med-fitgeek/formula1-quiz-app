# Récupération d'une image de base node JS 
FROM node:lts-alpine as build

# Installation du framework Vue
RUN npm install -g @vue/cli

# Création et positionnement du répertoire par défaut dans le container
WORKDIR /app

# Copie des fichiers référençant les dépendances de la machine hôte vers le container
# Ici, le répertoire cible est bien /app car il s'agit du WORKDIR
COPY package*.json ./

# Exposition du port 80
EXPOSE 80

# Installation des dépendances
RUN npm install

# Copie du reste du code source
COPY . .

# En local même dans Docker, l'API sera toujours accessible comme lors des devs
# Important : pour déployer l'image de prod, nous changerons ce chemin en /api
ENV VITE_API_URL=http://localhost:5000

# Construction du bundle de l'application
# Ceci va générer la version de prod de l'UI dans le répertoire /app/dist
RUN npm run build

# Étape 2 : Serveur NGINX pour les fichiers générés
FROM nginx:1.27.3

# Copie des fichiers générés vers le dossier NGINX par défaut
COPY --from=build /app/dist /usr/share/nginx/html

# Copie de la configuration personnalisée pour NGINX
COPY nginx.conf /etc/nginx/conf.d/default.conf



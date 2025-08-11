Chatbot Intelligent – CIEMS
📌 Contexte du projet
Ce projet a été réalisé dans le cadre d’un stage au sein de CIEMS, une entreprise marocaine spécialisée dans l’innovation et l’accompagnement stratégique.
L’objectif était de mettre en place un chatbot intelligent capable de répondre aux préoccupations des clients de manière rapide et pertinente, en automatisant les réponses aux questions fréquentes.

🎯 Objectifs
Fournir un service client automatisé disponible 24/7.

Réduire la charge de travail des conseillers.

Améliorer l’expérience utilisateur grâce à l’IA.

🛠️ Stack Technique
Langage : Python

Framework Web : Flask

Intelligence Artificielle : Réseaux de neurones (Deep Learning)

Bibliothèques principales :

NumPy, Pandas (manipulation de données)

PyTorch (entraînement et utilisation du modèle IA)

NLTK (traitement du langage naturel)

Flask (développement de l’interface et API)

📊 Données d’entraînement
Les données utilisées pour l’entraînement proviennent de Direct Assurance (France). [📄 Télécharger le PDF]([https://exemple.com/rapport.pdf](https://www.direct-assurance.fr/Sales/ContentStore/?filename=/Conditions_Generales_Assurance_Auto.pdf&tx=MzoxOjExOjE1OjE6MQ==))
Elles contiennent des dialogues clients permettant d’entraîner le modèle à reconnaître les intentions et à fournir des réponses adaptées.

🏗️ Architecture du projet
php
Copier
Modifier
├── __pycache__/           # Fichiers Python compilés
├── static/                # Fichiers statiques pour l’interface
│   ├── app.js             # Logique côté client (JavaScript)
│   ├── chatbox-icon.svg   # Icône du chatbot
│   └── style.css          # Styles CSS
├── templates/
│   └── index.html         # Page HTML principale
├── app.py                 # Point d’entrée Flask
├── chat.py                # Gestion des réponses du chatbot
├── data.pth               # Modèle entraîné sauvegardé
├── essai.py               # Script de test
├── intents.json           # Données d’entraînement (intents)
├── model.py               # Définition du modèle IA
├── nltk_code.py           # Prétraitement des données avec NLTK
├── train.py               # Script d’entraînement du modèle
└── README.md              # Documentation
🚀 Installation et exécution
1️⃣ Cloner le dépôt
bash
Copier
Modifier
git clone https://github.com/<ton-utilisateur>/<nom-du-repo>.git
cd <nom-du-repo>
2️⃣ Créer un environnement virtuel
bash
Copier
Modifier
python -m venv venv
source venv/bin/activate   # Sur macOS / Linux
venv\Scripts\activate      # Sur Windows
3️⃣ Installer les dépendances
bash
Copier
Modifier
pip install -r requirements.txt
4️⃣ Entraîner le modèle
bash
Copier
Modifier
python train.py
5️⃣ Lancer l’application
bash
Copier
Modifier
python app.py
Puis ouvrir un navigateur et aller sur :
http://127.0.0.1:5000/

📈 Fonctionnement
L’utilisateur pose une question via l’interface web.

Flask envoie la requête au modèle IA.

Le modèle prédit l’intention et renvoie la réponse correspondante.

🔮 Améliorations possibles
Ajout d’un support multilingue.

Enrichissement des données d’entraînement.

Intégration avec WhatsApp, Messenger, etc.

Hébergement sur un serveur cloud.

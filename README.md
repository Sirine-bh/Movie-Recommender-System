🎬 Movie Recommender System

Un système de recommandation de films basé sur la similarité du contenu (Content-Based Filtering), développé en Python avec Streamlit.

📌 Description du projet

Ce projet permet aux utilisateurs d’obtenir des recommandations personnalisées de films en se basant sur un film choisi dans une liste.
L'application utilise un modèle de similarité calculé à partir de plusieurs caractéristiques des films (genres, overview, keywords…).

Le système :

Charge un dataset de films prétraité

Calcule une matrice de similarité entre les films

Affiche des recommandations visuelles avec posters

Intègre un carousel de films populaires en haut

Fournit une interface moderne et simple grâce à Streamlit

Le site fonctionne localement et peut être déployé en ligne (Streamlit Cloud, Render…).

🚀 Fonctionnalités

✔️ Recommandation de films basée sur la similarité
✔️ Affichage des posters via l’API TMDB
✔️ Menu déroulant pour choisir un film
✔️ Affichage dynamique de 5 films similaires
✔️ Carousel de films populaires
✔️ Interface web simple et rapide avec Streamlit

🛠 Technologies Utilisées

Python 3

Streamlit

Pandas

Scikit-learn

Requests

TMDB API

Pickle (pour sauvegarder les matrices et le dataset)

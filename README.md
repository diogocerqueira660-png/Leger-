# Léger

Web app mobile de suivi de perte de poids, installable sur iPhone (Safari › Partager › Sur l'écran d'accueil).

- Budget calorique du jour (objectif − repas + activité), macros, repas
- Poids : courbe, moyenne 7 jours, tendance, bilan de la semaine
- Hydratation, jeûne intermittent, coach (FAQ hors ligne ou IA avec une clé API Anthropic)
- Connexions : Strava (OAuth), Apple Santé (Raccourci iOS ou export.xml), Open Food Facts

Toutes les données restent sur le téléphone (localStorage).

## Modifier l'app

Le code source est `src/app.html`. Après une modification, lancez `python3 build.py` (Python 3 + Pillow) : il régénère `index.html`, `manifest.webmanifest`, `sw.js` et les icônes à la racine, servis par GitHub Pages.

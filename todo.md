Lister les améliorations et les raccourcis pris à cause du temps
imparti :


> Choix technologique : FastAPI vs Flask
- J’ai choisi FastAPI pour gagner du temps :

- Swagger intégré automatiquement, sans configuration manuelle.

- Utilisation de Pydantic pour générer automatiquement les schémas de validation.

- Gestion native des types, des erreurs HTTP et des réponses JSON.

> Structure du projet
- J’ai regroupé tout le code dans un seul fichier main.py pour aller plus vite.

- En temps normal, il serait préférable de découper en modules (routes, logique métier, services...).

> Qualité du code
- Le code est fonctionnel, mais pas entièrement documenté.

- Les types sont bien définis pour plus de clarté.

- Les docstrings sont présents, mais pourraient être améliorés pour un projet en production.

> Implémentation de l’algorithme RPN
Pour l’algorithme de la calculatrice en notation polonaise inversée (RPN), je me suis inspiré de :
https://rosettacode.org/wiki/Parsing/RPN_calculator_algorithm#Python
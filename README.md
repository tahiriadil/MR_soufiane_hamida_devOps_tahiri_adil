# Centre de Bien-Être 🌿

Application Django de réservation de services bien-être (massage, spa, relaxation).

![CI/CD](https://github.com/tahiriadil/MR_soufiane_hamida_devOps_tahiri_adil/actions/workflows/ci-cd.yml/badge.svg)

##  Lancer avec Docker

```bash
docker compose up
```

L'application sera disponible sur : http://localhost:8000

##  Installation locale

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

##  Stack technique

- **Backend** : Django 5.2
- **Base de données** : SQLite
- **Conteneurisation** : Docker + Docker Compose
- **CI/CD** : GitHub Actions + Docker Hub

##  Branches Git

| Branche | Rôle |
|--------|------|
| `main` | Production |
| `develop` | Intégration |
| `feature/*` | Fonctionnalités |
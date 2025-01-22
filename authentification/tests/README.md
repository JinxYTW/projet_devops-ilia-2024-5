# Documentation des Tests d'Authentification API

## Introduction

Ce projet contient des tests pour l'authentification des utilisateurs d'une application Flask. Les tests vérifient le bon fonctionnement des routes `/auth/login` (connexion) et `/auth/sign_in` (inscription). Ils sont écrits avec `pytest` et utilisent un client Flask pour simuler les requêtes et vérifier les réponses.

## Pré-requis

- **Python 3.x**
- **Flask**
- **pytest**
- **pytest-flask**

Installez les dépendances avec :

```bash
pip install Flask pytest pytest-flask
```


## Tests d'Authentification

### Connexion Réussie

**Données envoyées** :
```json
{
  "username_or_email": "johndoe",
  "password": "password123"
}
```
**Résultat attendu** : Code `200` et un `token`.

### Connexion avec Informations Invalides

**Données envoyées** :
```json
{
  "username_or_email": "fakeuser",
  "password": "wrongpassword"
}
```
**Résultat attendu** : Code `401` et message `"Nom d'utilisateur ou mot de passe incorrect"`.

### Connexion avec Champs Manquants

**Données envoyées** : `{}`  
**Résultat attendu** : Code `400` et message `"Nom d'utilisateur ou mot de passe requis"`.

### Inscription Réussie

**Données envoyées** :
```json
{
  "nom": "Doe",
  "prenom": "John",
  "email": "john@example.com",
  "password": "password123",
  "username": "johndoe",
  "pseudo": "jd"
}
```
**Résultat attendu** : Code `200` et message `"Utilisateur créé avec succès"`.

### Inscription avec Utilisateur Déjà Existant

**Données envoyées** :
```json
{
  "nom": "Doe",
  "prenom": "Jane",
  "email": "jane@example.com",
  "password": "password123",
  "username": "johndoe",
  "pseudo": "janejd"
}
```
**Résultat attendu** : Code `409` et message `"Nom d'utilisateur ou email déjà utilisé"`.

### Inscription avec Champs Manquants

**Données envoyées** :
```json
{
  "nom": "Doe",
  "prenom": "John"
}
```
**Résultat attendu** : Code `400` et message `"Tous les champs sont obligatoires"`.

## Exécution des Tests

Pour exécuter les tests, utilisez la commande suivante :

```bash
pytest
```

Pour un test spécifique :

```bash
pytest -k "nom_du_test"
```

## Contribuer

1. Forkez le projet.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Soumettez une Pull Request avec vos modifications.


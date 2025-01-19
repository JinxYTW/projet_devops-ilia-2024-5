# Table des Matières

- [Accès à l'Application et Tests](#accès-à-lapplication-et-tests)
  - [Démarrage de l'Application](#démarrage-de-lapplication)
  - [Documentation Swagger](#documentation-swagger)
  - [Exécution des Tests](#exécution-des-tests)

- [API pour la gestion des Commentaires et Réactions](#api-pour-la-gestion-des-commentaires-et-réactions)
  - [Routes](#routes)
    - [Commentaires](#commentaires)
      - [Créer un commentaire sur un tweet](#créer-un-commentaire-sur-un-tweet)
      - [Récupérer les commentaires d’un tweet](#récupérer-les-commentaires-dun-tweet)
      - [Modifier un commentaire](#modifier-un-commentaire)
      - [Supprimer un commentaire](#supprimer-un-commentaire)
    - [Réactions](#réactions)
      - [Ajouter une réaction à un tweet](#ajouter-une-réaction-à-un-tweet)
      - [Ajouter une réaction à un commentaire](#ajouter-une-réaction-à-un-commentaire)
      - [Récupérer les réactions d’un tweet](#récupérer-les-réactions-dun-tweet)
      - [Récupérer les réactions d’un commentaire](#récupérer-les-réactions-dun-commentaire)
      - [Supprimer une réaction sur un tweet](#supprimer-une-réaction-sur-un-tweet)
      - [Supprimer une réaction sur un commentaire](#supprimer-une-réaction-sur-un-commentaire)
    - [Statistiques et Suivi](#statistiques-et-suivi)
      - [Récupérer les statistiques de réactions sur un tweet](#récupérer-les-statistiques-de-réactions-sur-un-tweet)
      - [Récupérer les statistiques de réactions sur un commentaire](#récupérer-les-statistiques-de-réactions-sur-un-commentaire)
    - [Authentification et Autorisation](#authentification-et-autorisation)
      - [Vérifier si un utilisateur a déjà réagi avec une réaction spécifique](#vérifier-si-un-utilisateur-a-déjà-réagi-avec-une-réaction-spécifique)
  - [Types de Réactions](#types-de-réactions)
  - [Conclusion](#conclusion)

- [Structure de Base de Données Redis](#structure-de-base-de-données-redis)
  - [Structure des Données](#structure-des-données)
    - [Commenter un tweet](#commenter-un-tweet)
    - [Commenter un commentaire](#commenter-un-commentaire)
    - [Réactions aux Tweets](#réactions-aux-tweets)
    - [Réactions aux Commentaires](#réactions-aux-commentaires)
    - [Utilisateurs ayant Réagi](#utilisateurs-ayant-réagi)
  - [Cas d'Usage et Opérations](#cas-dusage-et-opérations)

- [Guide de Contribution](#guide-de-contribution)
  - [Gestion des Tâches avec des Issues](#gestion-des-tâches-avec-des-issues)
    - [Création d’une Issue](#création-dune-issue)
  - [Création d'une Branche Associée](#création-dune-branche-associée)
  - [Développement Basé sur le TDD](#développement-basé-sur-le-tdd)
    - [Écriture des Tests Avant Développement](#écriture-des-tests-avant-développement)
    - [Exécution des Tests](#exécution-des-tests)
  - [Codage](#codage)
    - [Structure des Fichiers](#structure-des-fichiers)
    - [Intégration de Redis](#intégration-de-redis)
    - [Exemple de Code](#exemple-de-code)
    - [Règles de Codage](#règles-de-codage)
  - [Pull Request (PR)](#pull-request-pr)
    - [Création d'une PR](#création-dune-pr)
    - [Revue et Fusion](#revue-et-fusion)
  - [Bonnes Pratiques](#bonnes-pratiques)






# Accès à l'Application et Tests

## Démarrage de l'Application
Assurez-vous d'être dans le dossier reaction :

```bash
cd reaction/
```

Pour démarrer l'application, exécutez la commande suivante :

```bash
docker-compose up --build
```

Une fois démarrée, l'application sera accessible à l'adresse suivante :

- **Base URL de l'application**: [http://localhost:5000/](http://localhost:5000/)



## Documentation Swagger

La documentation Swagger de l'API est disponible à l'adresse suivante :

- **Lien Swagger**: [http://localhost/reactions/api/swagger/](http://localhost/reactions/api/swagger/)



## Exécution des Tests

Pour exécuter les tests, utilisez la commande suivante :

```bash
docker-compose -f docker-compose.test.yml up --build
```

Cette commande construira et lancera les conteneurs nécessaires à l'exécution des tests et exécuter automatiquement les tests.




# API pour la gestion des Commentaires et Réactions

Ce projet offre une API permettant de gérer les commentaires et les réactions (ou "likes") sur des tweets. L'API suit une architecture RESTful, avec des routes dédiées à la gestion des commentaires et des réactions des utilisateurs.

## Routes

### 1. **Commentaires**

#### Créer un commentaire sur un tweet
- **Route** : `POST /tweets/{tweet_id}/comments`
- **Description** : Permet à un utilisateur d’ajouter un commentaire à un tweet.
- **Corps de la requête** :
    ```json
    {
      "user_id": "12345",
      "content": "Ceci est un commentaire."
    }
    ```

#### Récupérer les commentaires d’un tweet
- **Route** : `GET /tweets/{tweet_id}/comments`
- **Description** : Récupère tous les commentaires associés à un tweet spécifique.
- **Réponse** :
    ```json
    [
      {
        "comment_id": "67890",
        "user_id": "12345",
        "content": "Ceci est un commentaire.",
        "created_at": "2023-01-10T12:34:56Z"
      }
    ]
    ```

#### Modifier un commentaire
- **Route** : `PUT /comments/{comment_id}`
- **Description** : Permet à un utilisateur de modifier son commentaire.
- **Corps de la requête** :
    ```json
    {
      "content": "Ceci est un commentaire modifié."
    }
    ```

#### Supprimer un commentaire
- **Route** : `DELETE /comments/{comment_id}`
- **Description** : Permet à un utilisateur de supprimer son commentaire.
- **Réponse** :
    ```json
    {
      "message": "Commentaire supprimé avec succès."
    }
    ```

### 2. **Réactions**

#### Ajouter une réaction à un tweet
- **Route** : `POST /tweets/{tweet_id}/reactions`
- **Description** : Permet à un utilisateur d’ajouter une réaction à un tweet.
- **Corps de la requête** :
    ```json
    {
      "user_id": "12345",
      "reaction": "like"
    }
    ```

#### Ajouter une réaction à un commentaire
- **Route** : `POST /comments/{comment_id}/reactions`
- **Description** : Permet à un utilisateur d’ajouter une réaction à un commentaire.
- **Corps de la requête** :
    ```json
    {
      "user_id": "12345",
      "reaction": "love"
    }
    ```

#### Récupérer les réactions d’un tweet
- **Route** : `GET /tweets/{tweet_id}/reactions`
- **Description** : Récupère toutes les réactions d’un tweet.
- **Réponse** :
    ```json
    [
      {
        "reaction_id": "11111",
        "user_id": "12345",
        "reaction": "haha",
        "created_at": "2023-01-10T12:45:00Z"
      }
    ]
    ```

#### Récupérer les réactions d’un commentaire
- **Route** : `GET /comments/{comment_id}/reactions`
- **Description** : Récupère toutes les réactions d’un commentaire.
- **Réponse** :
    ```json
    [
      {
        "reaction_id": "22222",
        "user_id": "67890",
        "reaction": "love",
        "created_at": "2023-01-10T12:50:00Z"
      }
    ]
    ```

#### Supprimer une réaction sur un tweet
- **Route** : `DELETE /tweets/{tweet_id}/reactions/{reaction_id}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un tweet.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Supprimer une réaction sur un commentaire
- **Route** : `DELETE /comments/{comment_id}/reactions/{reaction_id}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un commentaire.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

### 3. **Statistiques et Suivi**

#### Récupérer les statistiques de réactions sur un tweet
- **Route** : `GET /tweets/{tweet_id}/reactions/stats`
- **Description** : Récupère des statistiques sur les différentes réactions (nombre de chaque type de réaction) d’un tweet.
- **Réponse** :
    ```json
    {
      "like": 3,
      "love": 1
    }
    ```

#### Supprimer une réaction sur un tweet
- **Route** : `DELETE /tweets/{tweet_id}/reactions/{reaction_id}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un tweet.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Supprimer une réaction sur un commentaire
- **Route** : `DELETE /comments/{comment_id}/reactions/{reaction_id}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un commentaire.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Récupérer les statistiques de réactions sur un commentaire
- **Route** : `GET /comments/{comment_id}/reactions/stats`
- **Description** : Récupère des statistiques sur les différentes réactions (nombre de chaque type de réaction) d’un commentaire.
- **Réponse** :
    ```json
    {
      "like": 3,
      "love": 1
    }
    ```

### 4. **Authentification et Autorisation**

#### Vérifier si un utilisateur a déjà réagi avec une réaction spécifique
- **Route** : `GET /tweets/{tweet_id}/reactions/{user_id}`
- **Description** : Vérifie si un utilisateur spécifique a déjà réagi à un tweet avec une réaction particulière.
- **Réponse** :
    ```json
    {
      "has_reacted": true,
      "reaction": "like"
    }
    ```

## Types de Réactions

Les types de réactions sont :

- like
- love
- haha
- sad
- angry

## Conclusion

Cette API permet de gérer les interactions autour des tweets et des commentaires, en offrant des fonctionnalités de commentaires, réactions et statistiques. Elle est conçue pour être rapide et efficace, en permettant des opérations en temps réel avec un modèle de données flexible.



# Structure de Base de Données Redis

#### **1. Structure des Données**



##### **1.1. Commenter un twett**
- **Clés** :
  - `tweet:{tweet_id}:comments` (liste ordonnée des IDs de commentaires)
  - `comment:{comment_id}` (détails d'un commentaire)
- **Type** : *List* pour `tweet:{tweet_id}:comments`, *Hash* pour `comment:{comment_id}`
- **Données** :
  - Liste des commentaires :
    ```
    ["comment123", "comment124", "comment125"]
    ```
  - Détails d'un commentaire :
    ```json
    {
      "author_id": "user456",
      "content": "Ceci est un commentaire.",
      "parent_comment_id": null, 
      "created_at": "2025-01-10T10:05:00Z",
      "like_count": 5
    }
    ```

##### **1.2. Commenter un commentaires**
- **Clés** :
  - `comment:{command_id}:comments` (liste ordonnée des IDs de commentaires)
  - `comment:{comment_id}` (détails d'un commentaire)
- **Type** : *List* pour `comment:{command_id}:comments`, *Hash* pour `comment:{comment_id}`
- **Données** :
  - Liste des commentaires :
    ```
    ["comment123", "comment124", "comment125"]
    ```
  - Détails d'un commentaire :
    ```json
    {
      "author_id": "user456",
      "content": "Ceci est un commentaire.",
      "parent_comment_id": "command123", 
      "created_at": "2025-01-10T10:05:00Z",
      "like_count": 5
    }
    ```



---
##### **1.3. Réactions aux Tweets**
- **Clé** : `tweet:{tweet_id}:reactions_stat`
- **Type** : *Hash*
- **Données** :
```json
{
  "like": 20,
  "love": 5,
  "haha": 2,
  "sad": 1
}
```


---
##### **1.4. Réactions aux Commentaires**
- **Clé** : `comment:{comment_id}:reactions_stat`
- **Type** : *Hash*
- **Données** :
```json
{
  "like": 10,
  "angry": 1
}
```

---
##### **1.5. Utilisateurs ayant Réagi**
- **Clés** :
  - `tweet:{tweet_id}:reactions` ou `comment:{comment_id}:reactions` (liste ordonnée des IDs de réactions)
  - `reaction:{reaction_id}` (détails d'une réaction)
- **Type** : *Set*
- **Valeurs** :
```
["reaction123", "reaction456"]
```
- Détails d'une reaction :
    ```json
    {
      "reacted_user": "user456",
      "reaction": "haha", "love", "like", ...
      "created_at": "2025-01-10T10:05:00Z"
    }
    ```

#### **2. Cas d'Usage et Opérations**

1. **Ajouter un like à un tweet** :
   - Générer un `reaction_id`.
   - Incrémenter `like` dans `tweet:{tweet_id}:reactions_stat`.
   - Ajouter `reaction_id` dans `tweet:{tweet_id}:reactions` pour vérification.
   - Stocker les détails de la réaction `reaction:{reaction_id}`  

2. **Ajouter un commentaire à un tweet** :
   - Générer un `comment_id`.
   - Ajouter l'ID à `tweet:{tweet_id}:comments`.
   - Stocker les détails dans `comment:{comment_id}`.

3. **Réagir à un commentaire** :
   - Générer un `reaction_id`.
   - Incrémenter la réaction dans `comment:{comment_id}:reactions`.
   - Ajouter `reaction_id` dans `comment:{comment_id}:reactions`.
   - Stocker les détails du réaction `reaction:{reaction_id}`

4. **Ajouter un commentaire à un commentaire** :
   - Générer un `comment_id`.
   - Ajouter l'ID à `command:{command_id}:comments`.
   - Stocker les détails dans `comment:{comment_id}`.

5. **Obtenir un fil de discussion** :
   - Charger `tweet:{tweet_id}:comments`.
   - Charger chaque `comment:{comment_id}` et rechercher les sous-commentaires via `parent_comment_id`.






# Guide de Contribution au Développement de l'API Web de Réaction à un Tweet

Ce guide détaille les processus à suivre pour contribuer efficacement au développement de notre API, incluant l'intégration de Redis pour la gestion du db. Il couvre la gestion des tâches via les issues, la création de branches, le développement basé sur le Test-Driven Development (TDD), et la soumission de Pull Requests (PR).

## 1. Gestion des Tâches avec des Issues

### Création d’une Issue
1. **Définir la tâche** : Pour chaque nouvelle fonctionnalité ou correction de bug, créez une issue dans GitHub.
2. **Nom de l’issue** : Utilisez un titre clair et descriptif, tel que "Ajouter une route pour récupérer les utilisateurs".
3. **Description** : Incluez les spécifications détaillées, y compris les endpoints, les méthodes HTTP, et la logique métier attendue.
4. **Assignation** : Assignez l'issue à vous-même.

## 2. Création d'une Branche Associée

### Création de la Branche
1. **Utilisation du bouton GitHub** : Une fois l'issue créée, utilisez le bouton proposé par GitHub pour créer une branche associée.
2. **Convention de Nom des Branches** : Suivez le format `issue-[numéro]-[description]`, par exemple `issue-12-get-users-route`.

## 3. Développement Basé sur le TDD

### Écriture des Tests Avant Développement
1. **Fichier de Test** : Écrivez d'abord les tests pour chaque fonctionnalité dans le répertoire `tests/`.
   - Exemple : `tests/test_user_routes.py` pour les routes des utilisateurs.
2. **Structure des Tests** : Utilisez `pytest`. Chaque fichier de test doit couvrir les cas de test pour la fonctionnalité correspondante.

#### Exemple de Test (`tests/test_user_routes.py`)
```python
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)
```

### Exécution des Tests
1. **Lancer les Tests** : Assurez-vous que les tests échouent initialement, puis développez la fonctionnalité pour qu'ils passent.
   ```bash
   pytest tests/
   ```

## 4. Codage

### Structure des Fichiers
1. **Routes** : Chaque fichier de route se trouve dans `routes/` et contient les Blueprints et définitions des routes.
   - Exemple : `routes/user_routes.py` pour les routes utilisateurs.
2. **Services** : Placez la logique métier dans `services/`.
   - Exemple : `services/user_service.py` pour les services liés aux utilisateurs.

### Intégration de Redis
1. **Configuration de Redis** : Assurez-vous que Redis est installé et en cours d'exécution. Configurez l'application pour utiliser Redis comme base de données.
2. **Exemple de Connexion à Redis** :
   - Créez un fichier `db/redis_client.py` :
     ```python
     import redis

     def get_redis_client():
         return redis.Redis(host='localhost', port=6379, db=0)
     ```
3. **Utilisation de Redis dans un Service** :
   - Exemple dans `services/user_service.py` :
     ```python
     from db.redis_client import get_redis_client

     def get_all_users():
         client = get_redis_client()
         users = client.get('users')
         if users is None:
             # Simuler une récupération de la base de données
             users = []
         else:
             users = eval(users)
         return users
     ```

### Exemple de Code

#### Routes (`routes/user_routes.py`)
```python
from flask import Blueprint, jsonify
from app.services.user_service import get_all_users

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200
```

#### Services (`services/user_service.py`)
```python
from db.redis_client import get_redis_client

def get_all_users():
    client = get_redis_client()
    users = client.get('users')
    if users is None:
        # Exemple de données statiques (à remplacer par une requête à la base de données)
        users = []
    else:
        users = eval(users)
    return users
```

### Règles de Codage
1. **Séparation des Responsabilités** : 
   - Les **routes** gèrent les requêtes et réponses.
   - Les **services** contiennent la logique métier.
2. **Tests** : Testez localement votre code avant de soumettre une PR.

## 5. Pull Request (PR)

### Création d'une PR
1. **Push de la Branche** :
   ```bash
   git push origin issue-12-get-users-route
   ```
2. **Ouvrir une PR** : 
   - Créez une PR sur GitHub depuis votre branche vers la branche principale.
   - **Titre** : Utilisez le format `[Issue #12] Ajout de la route GET /users`.
   - **Description** : Décrivez les modifications apportées et incluez les détails pertinents.

### Revue et Fusion
1. **Revue de Code** : Une autre personne doit approuver la PR.
2. **Tests** : Vérifiez que tous les tests passent avant de fusionner.
3. **Fusion** : Fusionnez la PR une fois approuvée.

## 6. Bonnes Pratiques
- **Messages de Commit** : Soyez précis et utilisez un format cohérent.
  - Exemple : `feat: Ajout de la route GET /users`
- **Mise à Jour des Branches** : Maintenez votre branche à jour avec la branche principale.
   ```bash
   git pull origin main
   ```

En suivant ce guide, l'équipe peut collaborer efficacement tout en garantissant la qualité et la cohérence du code.
```
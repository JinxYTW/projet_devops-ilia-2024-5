# API pour la gestion des Commentaires et Réactions

Ce projet offre une API permettant de gérer les commentaires et les réactions (ou "likes") sur des tweets. L'API suit une architecture RESTful, avec des routes dédiées à la gestion des commentaires et des réactions des utilisateurs.

## Routes

### 1. **Commentaires**

#### Créer un commentaire sur un tweet
- **Route** : `POST /tweets/{tweetId}/comments`
- **Description** : Permet à un utilisateur d’ajouter un commentaire à un tweet.
- **Corps de la requête** :
    ```json
    {
      "userId": "12345",
      "content": "Ceci est un commentaire."
    }
    ```

#### Récupérer les commentaires d’un tweet
- **Route** : `GET /tweets/{tweetId}/comments`
- **Description** : Récupère tous les commentaires associés à un tweet spécifique.
- **Réponse** :
    ```json
    [
      {
        "commentId": "67890",
        "userId": "12345",
        "content": "Ceci est un commentaire.",
        "timestamp": "2023-01-10T12:34:56Z"
      }
    ]
    ```

#### Modifier un commentaire
- **Route** : `PUT /comments/{commentId}`
- **Description** : Permet à un utilisateur de modifier son commentaire.
- **Corps de la requête** :
    ```json
    {
      "content": "Ceci est un commentaire modifié."
    }
    ```

#### Supprimer un commentaire
- **Route** : `DELETE /comments/{commentId}`
- **Description** : Permet à un utilisateur de supprimer son commentaire.

### 2. **Réactions**

#### Ajouter une réaction à un tweet
- **Route** : `POST /tweets/{tweetId}/reactions`
- **Description** : Permet à un utilisateur d’ajouter une réaction à un tweet.
- **Corps de la requête** :
    ```json
    {
      "userId": "12345",
      "reaction": "like"
    }
    ```

#### Ajouter une réaction à un commentaire
- **Route** : `POST /comments/{commentId}/reactions`
- **Description** : Permet à un utilisateur d’ajouter une réaction à un commentaire.
- **Corps de la requête** :
    ```json
    {
      "userId": "12345",
      "reaction": "love"
    }
    ```

#### Récupérer les réactions d’un tweet
- **Route** : `GET /tweets/{tweetId}/reactions`
- **Description** : Récupère toutes les réactions d’un tweet.
- **Réponse** :
    ```json
    [
      {
        "reactionId": "11111",
        "userId": "12345",
        "reaction": "haha",
        "timestamp": "2023-01-10T12:45:00Z"
      }
    ]
    ```

#### Récupérer les réactions d’un commentaire
- **Route** : `GET /comments/{commentId}/reactions`
- **Description** : Récupère toutes les réactions d’un commentaire.
- **Réponse** :
    ```json
    [
      {
        "reactionId": "22222",
        "userId": "67890",
        "reaction": "love",
        "timestamp": "2023-01-10T12:50:00Z"
      }
    ]
    ```

#### Supprimer une réaction sur un tweet
- **Route** : `DELETE /tweets/{tweetId}/reactions/{reactionId}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un tweet.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Supprimer une réaction sur un commentaire
- **Route** : `DELETE /comments/{commentId}/reactions/{reactionId}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un commentaire.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

### 3. **Statistiques et Suivi**

#### Récupérer les statistiques de réactions sur un tweet
- **Route** : `GET /tweets/{tweetId}/reactions/stats`
- **Description** : Récupère des statistiques sur les différentes réactions (nombre de chaque type de réaction) d’un tweet.
- **Réponse** :
    ```json
#### Supprimer une réaction sur un tweet
- **Route** : `DELETE /tweets/{tweetId}/reactions/{reactionId}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un tweet.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Supprimer une réaction sur un commentaire
- **Route** : `DELETE /comments/{commentId}/reactions/{reactionId}`
- **Description** : Permet à un utilisateur de supprimer une réaction sur un commentaire.
- **Réponse** :
    ```json
    {
      "message": "Réaction supprimée avec succès."
    }
    ```

#### Récupérer les statistiques de réactions sur un commentaire
- **Route** : `GET /comments/{commentId}/reactions/stats`
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
- **Route** : `GET /tweets/{tweetId}/reactions/{userId}`
- **Description** : Vérifie si un utilisateur spécifique a déjà réagi à un tweet avec une réaction particulière.
- **Réponse** :
    ```json
    {
      "hasReacted": true,
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



############################################ BD ################################################
# Proposition de Structure de Base de Données Redis pour le Micro-Service de Réactions Twitter

#### **1. Structure des Données**


##### **1.1. Réactions aux Tweets**
- **Clé** : `tweet:{tweet_id}:reactions`
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
##### **1.2. Commentaires**
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

---
##### **1.3. Réactions aux Commentaires**
- **Clé** : `comment:{comment_id}:reactions`
- **Type** : *Hash*
- **Données** :
```json
{
  "like": 10,
  "angry": 1
}
```

---
##### **1.4. Utilisateurs ayant Réagi**
- **Clé** : `tweet:{tweet_id}:reacted_users` ou `comment:{comment_id}:reacted_users`
- **Type** : *Set*
- **Valeurs** :
```
["user123", "user456"]
```
- Détails d'une reaction :
    ```json
    {
      "reacted_user": "user456",
      "type": "haha", "love", "like"...,
      "created_at": "2025-01-10T10:05:00Z"
    }
    ```

#### **2. Cas d'Usage et Opérations**

1. **Ajouter un like à un tweet** :
   - Générer un `reaction_id`.
   - Incrémenter `like` dans `tweet:{tweet_id}:reactions`.
   - Ajouter l'utilisateur à `tweet:{tweet_id}:reacted_users` pour vérification.
   - Stocker les détails de la réaction `reaction:{reaction_id}`  

2. **Ajouter un commentaire** :
   - Générer un `comment_id`.
   - Ajouter l'ID à `tweet:{tweet_id}:comments`.
   - Stocker les détails dans `comment:{comment_id}`.

3. **Réagir à un commentaire** :
   - Générer un `reaction_id`.
   - Incrémenter la réaction dans `comment:{comment_id}:reactions`.
   - Ajouter l'utilisateur à `comment:{comment_id}:reacted_users`.
   - Stocker les détails du réaction `reaction:{reaction_id}`

4. **Obtenir un fil de discussion** :
   - Charger `tweet:{tweet_id}:comments`.
   - Charger chaque `comment:{comment_id}` et rechercher les sous-commentaires via `parent_comment_id`.





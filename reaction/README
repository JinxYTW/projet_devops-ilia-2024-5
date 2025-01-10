# API pour la gestion des Tweets, Commentaires et Réactions

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
      "reaction": "A"  // Par exemple, "A" pour "Like", "B" pour "Love", "C" pour "Haha", etc.
    }
    ```

#### Ajouter une réaction à un commentaire
- **Route** : `POST /comments/{commentId}/reactions`
- **Description** : Permet à un utilisateur d’ajouter une réaction à un commentaire.
- **Corps de la requête** :
    ```json
    {
      "userId": "12345",
      "reaction": "B"  // Par exemple, "A" pour "Like", "B" pour "Love", "C" pour "Haha", etc.
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
        "reaction": "A",
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
        "reaction": "B",
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
    {
      "A": 10,  // Par exemple, 10 Likes
      "B": 5,   // Par exemple, 5 Love
      "C": 8    // Par exemple, 8 Haha
    }
    ```

#### Récupérer les statistiques de réactions sur un commentaire
- **Route** : `GET /comments/{commentId}/reactions/stats`
- **Description** : Récupère des statistiques sur les différentes réactions (nombre de chaque type de réaction) d’un commentaire.
- **Réponse** :
    ```json
    {
      "A": 3,
      "B": 1
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
      "reaction": "A"
    }
    ```

## Types de Réactions

Les types de réactions sont définis par des lettres (A, B, C, etc.) pour chaque type :

- **A** : Like
- **B** : Love
- **C** : Haha
- **D** : Triste
- **E** : En colère

## Conclusion

Cette API permet de gérer les interactions autour des tweets et des commentaires, en offrant des fonctionnalités de commentaires, réactions et statistiques. Elle est conçue pour être rapide et efficace, en permettant des opérations en temps réel avec un modèle de données flexible.


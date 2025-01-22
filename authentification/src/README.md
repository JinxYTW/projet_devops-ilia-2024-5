# **Documentation des Routes**

Ce document décrit les différentes routes de l'API pour le microservice d'authentification. Toutes les routes sont protégées par **JWT** lorsque cela est mentionné.

---

## **Routes Authentification**

### **1. Rafraîchir un token JWT**
**Endpoint :**  
`POST /auth/refresh`

**Description :**  
Rafraîchit le token JWT si l'utilisateur est authentifié.

**Requête :**  
- **Headers :**  
  `Authorization: Bearer <token>`

**Réponse :**  
- **Code 200** :  
  ```json
  {
    "new_token": "eyJhbGciOi..."
  }
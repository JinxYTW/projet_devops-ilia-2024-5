import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app
from db.redis_client import get_redis_client

# Redis mock setup
@pytest.fixture
def redis_client():
    client = get_redis_client()
    client.flushdb()  # Nettoyer la base Redis avant chaque test
    return client

# Flask test client setup
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test pour la modification d'un commentaire
def test_update_comment(client, redis_client):
    tweet_id = "12345"
    
    # Ajouter un commentaire à Redis pour ce tweet
    comment_data = {
        "userId": "user1",
        "content": "This is a test comment"
    }
    response = client.post(f'/tweets/{tweet_id}/comments', json=comment_data)
    comment_id = response.get_json()['commentId']  # Récupérer l'ID du commentaire ajouté
    
    # Modifier le commentaire
    updated_data = {
        "content": "This is an updated test comment"
    }
    response = client.put(f'/comments/{comment_id}', json=updated_data)

    # Vérifier la réponse
    assert response.status_code == 200
    assert response.get_json() == {"message": "Comment updated successfully", "commentId": comment_id}

    # Vérifier que le commentaire a bien été mis à jour dans Redis
    comments = redis_client.lrange(f"comments:{tweet_id}", 0, -1)
    updated_comment = eval(comments[0].decode())  # Convertir le commentaire en dictionnaire
    assert updated_comment["content"] == "This is an updated test comment"

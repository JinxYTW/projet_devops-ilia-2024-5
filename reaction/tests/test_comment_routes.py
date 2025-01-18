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

# Test pour la création de commentaire
def test_create_comment(client, redis_client):
    tweet_id = "12345"
    data = {
        "userId": "user1",
        "content": "This is a test comment"
    }

    # Envoyer une requête POST pour créer un commentaire
    response = client.post(f'/tweets/{tweet_id}/comments', json=data)

    # Vérifier la réponse
    assert response.status_code == 201
    response_data = response.get_json()

    # Vérifier que la réponse contient le message et le commentId
    assert "message" in response_data
    assert response_data["message"] == "Comment added successfully"
    assert "commentId" in response_data

    # Vérifier que le commentaire est stocké dans Redis
    comments = redis_client.lrange(f"comments:{tweet_id}", 0, -1)
    assert len(comments) == 1

    # Convertir la chaîne de Redis en dictionnaire Python
    stored_comment = eval(comments[0].decode())

    # Vérifier que les données stockées correspondent à celles envoyées
    assert stored_comment["userId"] == data["userId"]
    assert stored_comment["content"] == data["content"]

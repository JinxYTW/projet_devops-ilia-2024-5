import pytest
import json
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app
from db.redis_client import get_redis_client

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def redis_client():
    client = get_redis_client()
    client.flushdb()  # Nettoyer la base Redis avant chaque test
    yield client
    client.flushdb()  # Nettoyer après chaque test

def test_delete_tweet_reaction(client, redis_client):
    # Set up test data
    tweet_id = "123"
    reaction_id = 1
    reaction_type = "like"
    
    # Add a reaction to Redis
    reaction_data = {
        "reacted_user": "user123",
        "reaction": reaction_type,
        "created_at": "2025-01-10T10:05:00Z"
    }
    redis_client.hset(f"tweet:{tweet_id}:reactions", reaction_id, json.dumps(reaction_data))
    
    # Initialize reactions_stat with counts
    redis_client.hset(f"tweet:{tweet_id}:reactions_stat", "like", 20)
    redis_client.hset(f"tweet:{tweet_id}:reactions_stat", "love", 5)
    redis_client.hset(f"tweet:{tweet_id}:reactions_stat", "haha", 2)
    redis_client.hset(f"tweet:{tweet_id}:reactions_stat", "sad", 1)

    # Simulate the DELETE request
    response = client.delete(f'/tweets/{tweet_id}/reactions/{reaction_id}')

    # Verify the response
    assert response.status_code == 200
    assert response.json == {"message": "Réaction supprimée avec succès."}

    # Verify that the reaction has been deleted from Redis
    assert not redis_client.hexists(f"tweet:{tweet_id}:reactions", reaction_id)

    # Verify that the reactions_stat has been updated correctly
    updated_like_count = int(redis_client.hget(f"tweet:{tweet_id}:reactions_stat", "like"))
    assert updated_like_count == 19  # Expecting decrement by 1

    # Optional: Check that other reaction counts remain unchanged
    assert int(redis_client.hget(f"tweet:{tweet_id}:reactions_stat", "love")) == 5
    assert int(redis_client.hget(f"tweet:{tweet_id}:reactions_stat", "haha")) == 2
    assert int(redis_client.hget(f"tweet:{tweet_id}:reactions_stat", "sad")) == 1


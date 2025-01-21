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
    client.flushdb()  # Clean Redis before each test
    yield client
    client.flushdb()  # Clean up after each test

def test_delete_reaction_comment(client, redis_client):
    # Set up test data
    comment_id = "67890"  # Example comment ID
    reaction_id = "12345"  # Example reaction ID
    reaction_type = "like"

    # Add a reaction to Redis associated with the comment
    reaction_data = {
        "reaction_id": reaction_id,
        "user_id": "user123",
        "reaction": reaction_type
    }
    redis_client.hset(f"comment:{comment_id}:reactions", reaction_id, json.dumps(reaction_data))

    # Add reactions_stat for the comment
    redis_client.hset(f"comment:{comment_id}:reactions_stat", reaction_type, 10)
    redis_client.hset(f"comment:{comment_id}:reactions_stat", "love", 5)
    redis_client.hset(f"comment:{comment_id}:reactions_stat", "haha", 2)
    redis_client.hset(f"comment:{comment_id}:reactions_stat", "sad", 1)

    # Simulate the DELETE request
    response = client.delete(f'/comments/{comment_id}/reactions/{reaction_id}')

    # Verify the response
    assert response.status_code == 200
    assert response.json == {"message": "Reaction deleted successfully"}

    # Verify that the reaction has been deleted from Redis
    assert not redis_client.hexists(f"comment:{comment_id}:reactions", reaction_id)

    # Verify that the reactions_stat has been updated correctly
    updated_reaction_count = int(redis_client.hget(f"comment:{comment_id}:reactions_stat", reaction_type))
    assert updated_reaction_count == 9  # Expecting decrement by 1

    # Optional: Check that other reaction counts remain unchanged
    assert int(redis_client.hget(f"comment:{comment_id}:reactions_stat", "love")) == 5
    assert int(redis_client.hget(f"comment:{comment_id}:reactions_stat", "haha")) == 2
    assert int(redis_client.hget(f"comment:{comment_id}:reactions_stat", "sad")) == 1

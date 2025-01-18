import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


#def test_get_users(client):
#    response = client.get('/users')
#    assert response.status_code == 200
#    assert isinstance(response.json, list)

def test_get_tweet_reactions(client):
    tweet_id = 1
    response = client.get(f'/tweets/{tweet_id}/reactions')
    
    assert response.status_code == 200
    assert isinstance(response.json, list)



#def test_get_tweet_reactions(client):
    # Simulate fetching reactions for a tweet with a non-existent endpoint
#    tweet_id = 1
#    response = client.get(f'/tweets/{tweet_id}/reactions')
    
    # Assert that the route does not exist or is not yet implemented
#    assert response.status_code == 404  # Expecting "Not Found"
#    assert response.json is None or response.json.get("error") == "Not Implemented"

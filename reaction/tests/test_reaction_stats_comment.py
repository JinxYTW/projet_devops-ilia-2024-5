import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_reaction_stats(client):
    # Simuler une requête GET vers la route de stats
    response = client.get('/comments/123/reactions/stats')
    
    assert response.status_code == 200
    assert response.json == {"like": 3, "love": 1}  # Selon les données attendues

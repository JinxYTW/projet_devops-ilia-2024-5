import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_delete_reaction_comment(client):
    # Préparation : Ajouter une réaction associée à un commentaire
    comment_id = "67890"  # ID fictif du commentaire
    reaction_id = "12345"  # ID fictif de la réaction
    client.post(f'/comments/{comment_id}/reactions', json={
        "reaction_id": reaction_id,
        "user_id": "user123",
        "reaction_type": "like"
    })

    # Suppression de la réaction
    response = client.delete(f'/comments/{comment_id}/reactions/{reaction_id}')

    # Vérifications
    assert response.status_code == 200  # Vérifie que l'opération est réussie
    assert response.json["message"] == "Reaction deleted successfully"

    # Vérifie que la réaction n'existe plus
    get_response = client.get(f'/comments/{comment_id}/reactions/{reaction_id}')
    assert get_response.status_code == 404  # La réaction ne devrait plus exister

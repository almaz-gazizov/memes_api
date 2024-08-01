def test_create_meme(client_public_api):
    response = client_public_api.post(
        "/memes/",
        json={
            "title": "Test Meme",
            "description": "This is a test meme",
            "image_url": "http://example.com/image.jpg"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Meme"
    assert data["description"] == "This is a test meme"
    assert data["image_url"] == "http://example.com/image.jpg"


def test_get_meme(client_public_api):
    response = client_public_api.get("/memes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Meme"


def test_update_meme(client_public_api):
    response = client_public_api.put(
        "/memes/1",
        json={
            "title": "Updated Meme",
            "description": "This is an updated meme",
            "image_url": "http://example.com/updated_image.jpg"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Meme"


def test_delete_meme(client_public_api):
    response = client_public_api.delete("/memes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Meme"

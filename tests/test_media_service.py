from io import BytesIO


def test_upload_image(client_media_service):
    image_content = BytesIO(b"fake image data")
    response = client_media_service.post(
        "/upload/",
        files={
            "file": ("test_image.jpg", image_content, "image/jpeg")
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "url" in data


def test_delete_image(client_media_service):
    filename = "test_image.jpg"
    response = client_media_service.delete(f"/delete/{filename}")
    assert response.status_code == 200
    data = response.json()
    assert data["detail"] == "File deleted"

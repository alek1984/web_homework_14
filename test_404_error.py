def test_404_error(client):
    response = client.get("/non-existent-url/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


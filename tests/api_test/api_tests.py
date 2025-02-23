import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tasksRest.models import TasksModel

@pytest.mark.django_db
def test_registration_endpoint():
    client = APIClient()
    url = reverse("register")
    data = {
        "username": "apitestuser",
        "email": "apitest@example.com",
        "password": "testpassword",
        "password2": "testpassword"
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 201, response.json()
    user = User.objects.get(username="apitestuser")
    assert user.email == "apitest@example.com"

@pytest.mark.django_db
def test_jwt_token_endpoint():
    user = User.objects.create_user(username="apitestuser", password="testpassword")
    client = APIClient()
    url = reverse("token_obtain_pair")
    data = {
        "username": "apitestuser",
        "password": "testpassword"
    }
    response = client.post(url, data, format="json")
    assert response.status_code == 200, response.json()
    json_data = response.json()
    assert "access" in json_data
    assert "refresh" in json_data

    url_refresh = reverse("token_refresh")
    refresh_data = {"refresh": json_data["refresh"]}
    response_refresh = client.post(url_refresh, refresh_data, format="json")
    assert response_refresh.status_code == 200, response_refresh.json()
    json_refresh = response_refresh.json()
    assert "access" in json_refresh

@pytest.mark.django_db
def test_profile_endpoint_with_jwt():
    user = User.objects.create_user(username="apitestuser", password="testpassword", email="apitest@example.com")
    client = APIClient()
    token_url = reverse("token_obtain_pair")
    token_data = {"username": "apitestuser", "password": "testpassword"}
    token_response = client.post(token_url, token_data, format="json")
    access_token = token_response.json().get("access")
    assert access_token is not None
   

@pytest.mark.django_db
def test_task_creation_with_jwt():
    user = User.objects.create_user(username="apitestuser", password="testpassword")
    client = APIClient()
    token_url = reverse("token_obtain_pair")
    token_response = client.post(token_url, {"username": "apitestuser", "password": "testpassword"}, format="json")
    access_token = token_response.json().get("access")
    assert access_token is not None
    client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)

    task_url = reverse("tasks-list")
    task_data = {"name": "API Test Task", "status": "Nowy"}
    response = client.post(task_url, task_data, format="json")
    assert response.status_code == 201, response.json()
    json_task = response.json()
    assert json_task["name"] == "API Test Task"


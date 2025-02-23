import pytest
from django.contrib.auth.models import User
from accounts.serializers import RegisterSerializer

@pytest.mark.django_db
def test_register_serializer_valid():
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "secret123",
        "password2": "secret123"
    }
    serializer = RegisterSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    user = serializer.save()
    assert user.username == "newuser"
    assert user.email == "newuser@example.com"

@pytest.mark.django_db
def test_register_serializer_password_mismatch():
    data = {
        "username": "newuser",
        "email": "newuser@example.com",
        "password": "secret123",
        "password2": "different"
    }
    serializer = RegisterSerializer(data=data)
    assert not serializer.is_valid()
    assert "password" in serializer.errors


import pytest
from django.contrib.auth.models import User
from tasksRest.models import TasksModel

@pytest.mark.django_db
def test_create_task():
    user = User.objects.create_user(username="testuser", password="secret")

    task = TasksModel.objects.create(
        name="Test Task",
        description="Description of test task",
        status="Nowy",
        assigned_user=user
    )

    assert task.name == "Test Task"
    assert task.status == "Nowy"
    assert task.assigned_user == user

@pytest.mark.django_db
def test_update_task_status():
    user = User.objects.create_user(username="testuser2", password="secret")
    task = TasksModel.objects.create(name="Task to update", status="Nowy", assigned_user=user)

    task.status = "W toku"
    task.save()

    updated_task = TasksModel.objects.get(id=task.id)
    assert updated_task.status == "W toku"


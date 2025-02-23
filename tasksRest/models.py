from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

class TasksModel(models.Model):
    STATUS_CHOICES = (
            ('Nowy', 'Nowy'),
            ('W toku', 'W toku'),
            ('Rozwiązany', 'Rozwiązany'),
    )

    history = HistoricalRecords()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Nowy')
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="tasks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

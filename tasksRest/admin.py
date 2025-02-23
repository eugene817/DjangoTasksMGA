from django.contrib import admin
from .models import TasksModel
from simple_history.admin import SimpleHistoryAdmin

class TasksAdmin(SimpleHistoryAdmin):
    history_list_display = ['status', 'assigned_user']
    list_display = ['id', 'name', 'status', 'assigned_user', 'updated_at']
    search_fields = ['name', 'assigned_user__username']

admin.site.register(TasksModel, SimpleHistoryAdmin)

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasksRest.views import TasksViewSet


router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

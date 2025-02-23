from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasksRest.views import TasksViewSet


router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),

    # main api endpoint
    path('api/', include(router.urls)),

    # tokens and registration
    path('api/accounts/', include('accounts.urls')),

 
]

from django.db.models.deletion import models
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TasksModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TasksSerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer(read_only=True)
    assigned_user_id = serializers.PrimaryKeyRelatedField(
            queryset=User.objects.all(),
            source='assigned_user',
            write_only=True,
            allow_null=True,
            required=False
    )

    class Meta:
        model = TasksModel
        fields = [
                'id',
                'name',
                'description',
                'status',
                'assigned_user',
                'assigned_user_id',
                'created_at',
                'updated_at',
                ]


class TaskHistorySerializer(serializers.ModelSerializer):
    history_user_username = serializers.SerializerMethodField()

    class Meta:
        model = TasksModel.history.model
        fields = [
            'id',
            'name',
            'description',
            'status',
            'assigned_user',
            'history_id',
            'history_date',
            'history_user',  
            'history_user_username',
            'history_type',  # ' ~': change, '+' : create, '-' : delete
        ]
    
    def get_history_user_username(self, obj):
        if obj.history_user:
            return obj.history_user.username
        return None

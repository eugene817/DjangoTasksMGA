from rest_framework import viewsets, filters, decorators, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TasksModel
from .serializers import TasksSerializer, TaskHistorySerializer

class TasksViewSet(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    serializer_class = TasksSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'status', 'assigned_user__username']

    def get_queryset(self):
        queryset = super().get_queryset()  
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status__icontains=status_param)
        return queryset
    
    @decorators.action(detail=True, methods=['get'], url_path='history')
    def get_history(self, request, pk=None):
        task = self.get_object()
        history_qs = task.history.all().order_by('-history_date')
        serializer = TaskHistorySerializer(history_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


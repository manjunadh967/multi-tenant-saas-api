from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(generics.ListCreateAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']

    def get_queryset(self):

        return Task.objects.filter(
            project__organization=self.request.user.organization
        )

    def get_serializer_context(self):

        return {
            'request': self.request
        }


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    lookup_field = 'id'

    def get_queryset(self):

        return Task.objects.filter(
            project__organization=self.request.user.organization
        )

    def get_serializer_context(self):

        return {
            'request': self.request
        }

    def destroy(self, request, *args, **kwargs):

        if request.user.role != 'admin':
            return Response(
                {'error': 'Only admins can delete tasks'},
                status=403
            )

        return super().destroy(request, *args, **kwargs)
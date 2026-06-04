from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Project
from .serializers import ProjectSerializer


class ProjectView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        projects = Project.objects.filter(organization=request.user.organization)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        
        serializer = ProjectSerializer(data=request.data, context={'request':request})
    
        if serializer.is_valid():
            project = serializer.save()
            response_serializer = ProjectSerializer(project)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)




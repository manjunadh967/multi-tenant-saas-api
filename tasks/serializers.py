from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'project',
            'assigned_to',
            'created_at'
        ]

    def validate_project(self, project):

        request = self.context.get('request')

        if project.organization != request.user.organization:
            raise serializers.ValidationError(
                "You cannot access this project"
            )

        return project

    def validate_assigned_to(self, user):

        request = self.context.get('request')

        if user.organization != request.user.organization:
            raise serializers.ValidationError(
                "You cannot assign users from another organization"
            )

        return user
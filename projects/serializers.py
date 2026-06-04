from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'created_at']

    def create(self, validated_data):

        request = self.context.get('request')

        project = Project.objects.create(
            name = validated_data['name'],
            description = validated_data.get('description', ''),
            organization = request.user.organization,
            created_by = request.user
        )

        return project
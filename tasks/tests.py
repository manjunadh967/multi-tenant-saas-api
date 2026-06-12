from rest_framework.test import APITestCase
from rest_framework import status

from organizations.models import Organization
from accounts.models import User
from projects.models import Project
from tasks.models import Task


class TaskPermissionTest(APITestCase):

    def setUp(self):

        self.organization = Organization.objects.create(
            name='Test Company'
        )

        self.user = User.objects.create_user(
            email='user@test.com',
            password='password123',
            username='Normal User',
            organization=self.organization,
            role='member'
        )

        self.project = Project.objects.create(
            name='Project',
            organization=self.organization,
            created_by=self.user
        )

        self.task = Task.objects.create(
            title='Task 1',
            project=self.project
        )

        response = self.client.post(
            '/api/login/',
            {
                'email': 'user@test.com',
                'password': 'password123'
            }
        )

        token = response.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )

    def test_member_cannot_delete_task(self):

        response = self.client.delete(
            f'/api/tasks/{self.task.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
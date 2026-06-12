from rest_framework.test import APITestCase
from rest_framework import status

from accounts.models import User
from organizations.models import Organization


class ProjectAPITest(APITestCase):

    def setUp(self):
        self.organization = Organization.objects.create(name='Test Company')
        self.user = User.objects.create(
            email='Test@email.com',
            username='Test',
            organization=self.organization,
            role='admin'
        )
        self.user.set_password('test@123')
        self.user.save()
        
        from rest_framework_simplejwt.tokens import RefreshToken

        refresh = RefreshToken.for_user(self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}'
        )
        

    def test_create_project(self):
        response = self.client.post('/api/projects/',
                                        {'name': 'Mobile App',
                                        'description': 'Build company mobile app'
                                        }, format='json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
from django.contrib.auth.models import User, Permission
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

class UserTestCase(APITestCase):
    """
    Test for user
    """
    def setUp(self) -> None:
        
        self.user = User.objects.create_user(username= "admintest", password= "admintest123", email= "admin_test@admin.com")
        self.users = User.objects.all()
        self.token = Token.objects.get(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
    def test_get_all_users(self):
        """
        Test UserViewSet list method
        """
        
        response = self.client.get(f'/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_one_user(self):

        for user in self.users:
            response = self.client.get(f'/users/{user.pk}/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        

from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from consumer.models import Product, Category
# Create your tests here.


class ProductTestCase(APITestCase):
    """
    Test for Product
    """

    def setUp(self) -> None:
        Category.objects.create(name="Refrigerante")
        Product.objects.create(name="Coca-Cola", category = Category.objects.first(), price="12.50")
        Product.objects.create(name="Guaraná Antarctica", category = Category.objects.first(), price="11.50")
        Product.objects.create(name="Sufresh", category = Category.objects.first(), price="12.50")
        Product.objects.create(name="Mineirinho", category = Category.objects.first(), price="2.50")
        self.products = Product.objects.all()
        self.user = User.objects.create_user(username= "admintest", password= "admintest123", email= "admin_test@admin.com")
        self.token = Token.objects.get(user = self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_get_all_product(self):
        self.assertEqual(self.products.count(), 4)
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_product(self):
        data = {"name":'test', "category":"1", "price":"11.50"}
        response = self.client.post(f'/products/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

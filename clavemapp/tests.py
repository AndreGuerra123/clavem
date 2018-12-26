from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from .models import Product, ProductImage
# Create your tests here.

# class ProductModelTestCase(TestCase):
#     """This class defines the test suite for the product model."""

#     def setUp(self):
#         """Define the test client and other test variables."""
#         self.product_name = "Product name."
#         self.product_description = "Product description."
#         self.product_price = 22.22
#         self.product_quantity = 2

#         self.product = Product(name=self.product_name, description=self.product_description, price=self.product_price,quantity=self.product_quantity)

#     def test_model_can_create_a_product(self):
#         """Test the product model can create a product entry."""
#         old_count = Product.objects.count()
#         self.product.save()
#         new_count = Product.objects.count()
#         self.assertEqual(old_count+1, new_count)

class ProductAPITestCase(APITestCase):
    """Test suite for the product api."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.user = get_user_model().objects.create_user(
            'test',
            'test@test.com',
            'test',is_staff=True)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.client.post(reverse('api_product'),{'title': 'a','description':'b','cost':22.22,'stock':2})
        self.product = Product.objects.all().first()

    def test_api_can_create_a_product(self):
        """Test the api has product creation capability."""
        response = self.client.post(reverse('api_product'),{'title': 'd','description':'e','cost':12.22,'stock':0})        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_the_list_of_products(self):
        """Test the api has products list get capability."""        
        response = self.client.get(reverse('api_product'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_product(self):
        """Test the api can get a given product."""
        product = Product.objects.all().first()
        response = self.client.get(
            reverse('api_product',
            kwargs={'pk': self.product.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_a_product(self):
        """Test the api can update a given product."""
        product = Product.objects.all().first()
        change_product = {'title': 'd','description':'e','cost':12.22,'stock':0}
        res = self.client.put(
            reverse('api_product', kwargs={'pk': self.product.id}),
            change_product)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_product(self):
        """Test the api can delete a given product."""
        product = Product.objects.first()
        response = self.client.delete(
            reverse('api_product', kwargs={'pk': self.product.id}),
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)       
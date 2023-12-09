from django.test import TestCase
from django.urls import reverse
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='This is a test product.',
            price=20.0,
            quantity_in_stock=10,
        )

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_product_list_view(self):
        url = reverse('product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_product_create_view(self):
        url = reverse('product_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        data = {
            'name': 'New Product',
            'description': 'This is a new product.',
            'price': 30.0,
            'quantity_in_stock': 5,
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Product.objects.count(), 2)  # Assuming you have one product created in setUp

    # Add more tests as needed for other views and functionalities


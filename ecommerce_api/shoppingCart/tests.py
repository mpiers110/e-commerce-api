from django.test import TestCase
from .models import Cart, CartProduct
from products.models import Product
from accounts.models import CustomUser

class CartTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            name='testuser',
            email='test@gmail.com'
        )
        self.cart = Cart.objects.create(
            customer=self.user
        )

    def test_cart_str_method(self):
        expected_str = f"{self.user.name}'s Cart"
        self.assertEqual(str(self.cart), expected_str)

    def test_cartProduct_str_method(self):
        product = Product.objects.create(name='Test Product', price=10.0, quantity_in_stock=5)
        cart_product = CartProduct.objects.create(product=product, cart=self.cart)
        expected_str = f"{product.name} in {self.cart}"
        self.assertEqual(str(cart_product), expected_str)

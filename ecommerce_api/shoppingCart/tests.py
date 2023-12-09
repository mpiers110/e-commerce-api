from django.test import TestCase
from .models import Cart, CartProduct
from products.models import Product
from accounts.models import CustomUser

# Create your tests here.
class CartTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(
            name='testuser',
            email='test@gmail.com'
        )
        self.cart = Cart.objects.create(
            customer=self.user
        )

    def test_cart_creation(self):
        self.assertEqual(str(self.cart), f'{self.user.name}\'s Cart')

    def test_cartProduct_creation(self):
        product = Product.objects.create(name='Test Product', price=10.0, quantity_in_stock=5)
        cartProduct = CartProduct.objects.create(product=product, cart=self.cart)
        self.assertEqual(str(cartProduct), f'{product.name} in {self.cart}')



#from django.contrib.auth.decorators import login_required #require login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartProduct
from products.models import Product
#from accounts.models import CustomUser

# Create your views here.
#@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(customer=user)

    # Check if the product is already in the cart
    cart_product, product_created = CartProduct.objects.get_or_create(cart=cart, product=product)

    # If the product is already in the cart, increase the quantity
    if not product_created:
        cart_product.quantity += 1
        cart_product.save()

    return redirect('product_detail', pk=product_id)

#@login_required
def view_cart(request):
    user = request.user

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(customer=user)

    cart_products = CartProduct.objects.filter(cart=cart)

    return render(request, 'view_cart.html', {'cart': cart, 'cart_products': cart_products})

#@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user

    # Get the user's cart
    cart = get_object_or_404(Cart, customer=user)

    # Remove the product from the cart
    CartProduct.objects.filter(cart=cart, product=product).delete()

    return redirect('view_cart')

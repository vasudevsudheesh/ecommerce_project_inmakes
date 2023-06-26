from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    item_count = 0
    if "admin" in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            # Add your remaining code here to perform the desired actions
            # For example, you can iterate over the cart_items and update the item_count

            # Example code to update item_count:
            for cart_item in cart_items:
                item_count += cart_item.quantity

            # Return the item_count or any other desired result
        except Cart.DoesNotExist:
            item_count = 0
        return dict(item_count=item_count)

from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_detail, name="cart_detail"),
    path("add/<int:product_id>/", views.add_cart, name="add_cart"),
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
    path("full_remove/<int:product_id>/", views.full_remove, name="full_remove"),

    # path("<slug:c_slug>/", views.allprodcat, name="products_by_category"),
    # path("<slug:c_slug>/<slug:product_slug>/", views.prodetail, name="prodcatdetail"),
    # # path("base/", views.base_view, name="base"),
    # path('blog/', views.blog, name='blog'),
]

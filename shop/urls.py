from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.allprodcat, name="allprodcat"),
    path("<slug:c_slug>/", views.allprodcat, name="products_by_category"),
    path("<slug:c_slug>/<slug:product_slug>/", views.prodetail, name="prodcatdetail"),
    # path("base/", views.base_view, name="base"),
    # path('blog/', views.blog, name='blog'),
    # path('blog/<int:post_id>/', views.blog_post, name='blog_post'),
]

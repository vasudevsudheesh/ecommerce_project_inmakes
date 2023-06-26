from django.urls import path
from . import views

app_name = "search_app"
urlpatterns = [
    path("", views.searchresults, name="searchresults"),
    # path('blog/<int:post_id>/', views.blog_post, name='blog_post'),
]

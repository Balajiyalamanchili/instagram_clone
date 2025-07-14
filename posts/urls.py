from django.urls import path
from . import views


urlpatterns= [
    path('posts/',views.show_posts,name='show_posts'),
    path('create_post/',views.create_post ,name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]
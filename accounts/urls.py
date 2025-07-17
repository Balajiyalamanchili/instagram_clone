from django.urls import path
from . import views


urlpatterns =[
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('',views.login_view,name='login'),
    path('profile/',views.profile_view,name='profile'),
    path('show_user_profile/<str:username>',views.show_user_profile,name='show_user_profile'),
    path('follow_unfollow/<int:follow_id>',views.follow_unfollow,name='follow_unfollow'),
    path('show_all_users/',views.show_all_users,name='show_all_users'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/', views.edit_profile, name='edit_profile'),
]

 

from django.urls import path
from . import views


urlpatterns = [
    path('show_reels/',views.show_reels,name='show_reels'),
]


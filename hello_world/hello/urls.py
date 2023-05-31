from django.urls import path
from hello import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<str:who>', views.home_who, name='home_who'),
]
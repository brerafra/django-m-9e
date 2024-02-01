from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('filtro/', filter_test, name='filter_test'),
]

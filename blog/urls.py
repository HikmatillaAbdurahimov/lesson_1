from django.urls import path
from .views import home,register,groups,login,account

urlpatterns = [
    path('',home, name='home'),
    path('register/', register, name='register'),
    path('groups/', groups, name='groups'),
    path('login/', login, name='login'),
    path('account/', account, name='account'),
]
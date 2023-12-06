from django.urls import path
from .views import register, log_in

app_name = 'Accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
]


































from django.urls import path
from .views import UserRegistrationView,UserRegistrationVerifyView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/verify/', UserRegistrationVerifyView.as_view(), name='register-verify'),
]
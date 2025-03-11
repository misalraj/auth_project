from django.urls import path
from .views import UserRegistrationView,UserRegistrationVerifyView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/verify/', UserRegistrationVerifyView.as_view(), name='register-verify'),
    path('login/', UserLoginView.as_view(), name='login'),
]
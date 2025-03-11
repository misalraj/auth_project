from django.urls import path
from .views import UserRegistrationView,UserRegistrationVerifyView, UserLoginView, UserDetailsView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('register/verify/', UserRegistrationVerifyView.as_view(), name='register-verify'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserDetailsView.as_view(), name='me'),
]
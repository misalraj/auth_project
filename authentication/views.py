# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully. Please check your email for OTP."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRegistrationVerifyView(APIView):
    def post(self, request):
        # Implement OTP verification logic here
        return Response({"message": "User verified successfully."}, status=status.HTTP_200_OK)
    
class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            response = Response({"message": "Login successful."}, status=status.HTTP_200_OK)
            response.set_cookie('auth_token', 'your_auth_token', httponly=True, secure=True)
            return response
        return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'email': user.email,
            # Add other user details here
        })
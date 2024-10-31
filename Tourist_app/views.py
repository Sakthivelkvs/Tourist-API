

from .models import TouristApp,AdminRegister,Login

from rest_framework import generics

from .serializers import TouristSerializer,AdminSerializer,LoginSerializer

from rest_framework.permissions import AllowAny

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


# Create your views here.


class CreateTouristPlace(generics.ListCreateAPIView):
    queryset = TouristApp.objects.all()
    serializer_class = TouristSerializer
    permission_classes = [AllowAny]




class ViewTouristPlace(generics.RetrieveAPIView):
    queryset = TouristApp.objects.all()
    serializer_class = TouristSerializer


class UpdateTouristPlace(generics.RetrieveUpdateAPIView):
    queryset = TouristApp.objects.all()
    serializer_class = TouristSerializer


class DeleteTouristPlace(generics.RetrieveDestroyAPIView):
    queryset = TouristApp.objects.all()
    serializer_class = TouristSerializer


class RegisterAdmin(generics.ListCreateAPIView):
    queryset = AdminRegister.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        # Save the new AdminRegister instance
        admin_instance = serializer.save()

        # Create a corresponding Login instance
        Login.objects.create(
            username=admin_instance.email,
            password=admin_instance.password
        )


class ViewAdmin(generics.RetrieveAPIView):
    queryset = AdminRegister.objects.all()
    serializer_class = AdminSerializer


class ViewLogin(generics.ListAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]


class VerifyLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            login = Login.objects.get(username=username, password=password)
            return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
        except Login.DoesNotExist:
            return Response({"message": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
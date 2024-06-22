from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import login
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import SignINSerializer, BookSerializer
from .models import User, Book
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor


class Home(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # authentication_classes = SessionAuthentication
    permission_classes = [IsAuthor]


# class SignIn(APIView):
#
#     def post(self, request):
#
#         serializer = SignINSerializer(data=request.data)
#
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]
#             login(request, user)
#             return redirect(reverse("home"))
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SignIn(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = SignINSerializer
#
#     @action(detail=False, methods=['post'], url_path='signin')
#     def signin(self, request):
#         serializer = SignINSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)
#             return Response({'message': 'Logged in successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SignIn(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = SignINSerializer
#
#     @action(detail=False, methods=["POST"], url_path="signin")
#     def signin(self, request):
#         serializer = SignINSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]
#             login(request, user)
#             return Response(
#                 {"message": "Logged in successfully"}, status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# tasks/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions # Import permissions module
from .permissions import IsOwnerOrReadOnly # Assuming you have this custom permission
# from .permissions import IsAdminOrReadOnly # Keep if you plan to use it elsewhere

from .models import Task
from .serializers import TaskSerializer, UserSerializer # Corrected typo: UserSerializer
from django.contrib.auth.models import User

# Filter backends for TaskListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# --- API View for User Registration ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,) # Allow any user (even unauthenticated) to register
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED) # Return 201 Created for successful registration


# --- API View for Task Listing and Creation ---
class TaskListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can list/create tasks

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']
    search_fields = ['title', 'description'] # Search by title or description
    ordering_fields = ['created_at', 'title', 'completed'] # Order by these fields

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(owner=self.request.user).order_by('-created_at') # Order by latest first
        return Task.objects.none()
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk' 
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(owner=self.request.user)
        return Task.objects.none() 

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny] 
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password) # Pass request to authenticate

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
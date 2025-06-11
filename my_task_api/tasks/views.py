# tasks/views.py

from rest_framework import generics, status 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token 
from django.contrib.auth import authenticate 
from rest_framework import permissions 
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


from .models import Task
from .serializers import TaskSerializer 
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters 


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed', 'owner'] 
    search_fields = ['title', 'description'] 
    ordering_fields = ['created_at', 'title', 'completed'] 


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly] 


class LoginAPIView(APIView):
    permission_classes = [] 
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
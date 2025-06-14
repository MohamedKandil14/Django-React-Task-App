"""
URL configuration for my_task_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# my_task_api/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from tasks.views import RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  
      # URLs للتوثيق
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
     path('api-auth/', include('rest_framework.urls')), 
    path('api/login/', obtain_auth_token, name='api_token_auth'), 
    path('api/register/', RegisterView.as_view(), name='api_register'),
    path('api/', include('tasks.urls')), 
]

"""Project URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from api.views import api_root


apipatterns = [
    path('', include('rest_framework.urls')),
    path('', api_root, name='api-root'),
    path('users/', include('api.profiles.urls'), name='api-users'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns), name='api'),
]


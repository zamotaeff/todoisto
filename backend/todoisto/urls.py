from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('bot.urls')),
    path('core/', include('core.urls')),
    path('goals/', include('goals.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('api-auth/', include('rest_framework.urls')),
]

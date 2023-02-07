# from split_settings.tools import include
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_teasers.api.urls')),
]

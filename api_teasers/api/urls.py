from django.urls import include, path

urlpatterns = [
    path('v1/', include('api_teasers.api.v1.urls')),
]
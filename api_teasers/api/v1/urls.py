from django.urls import path

from api_teasers.api.v1 import views


urlpatterns = [
    path('set_teaser_status/', views.SetTeaserStatusApi.as_view(), name='set_teaser_status_api'),
    path('api-token-auth/', views.ObtainAuthTokenWithCSRFToken.as_view(), name='api_token_auth'),
    
] 

from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from django.middleware.csrf import get_token

from django.views import View
from ...models import Teaser


@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
class SetTeaserStatusApi(View):

    """
    Teaser status change. 
    In the body of the request, specify teaser_ids and status, 
    in the Authorization header with a token, in the csrf_token cookie
    """

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        teaser_ids = request.POST.getlist('teaser_ids')
        status = request.POST.get('status')

        if not teaser_ids or not status:
            return HttpResponseBadRequest("'teaser_ids' and 'status' are required fields")
        
        if status not in ["approved", "declined"]:
            return HttpResponseBadRequest("'status' can only be 'approved' or 'declined'")

        Teaser.objects.filter(id__in=teaser_ids).update(status=status)
        return JsonResponse({'success': True})


class ObtainAuthTokenWithCSRFToken(ObtainAuthToken):

    """Authentication. Getting a token and csrf token"""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')
        csrf_token = get_token(request)
        response = Response({'token': token}, status=status.HTTP_200_OK)
        response.set_cookie('csrftoken', csrf_token)
        return response
from django.utils import timezone
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.exceptions import InvalidToken


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if 'Authorization' in request.headers:
            try:
                user = authentication.JWTAuthentication().authenticate(request)[0]
            except InvalidToken:
                return JsonResponse({"detail": "Given token not valid for any token type",
                                     "code":"token_not_valid",
                                     "messages":[
                                         {"token_class": "AccessToken",
                                          "token_type": "access",
                                          "message": "Token is invalid or expired"}
                                     ]},
                                    status=401)

            cache.set(user.username, timezone.now())
        return None

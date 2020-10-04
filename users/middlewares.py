from django.utils import timezone
from django.core.cache import cache


class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        if hasattr(request, 'user') and request.user.is_authenticated:
            cache.set(request.user.username, timezone.now())
        return None

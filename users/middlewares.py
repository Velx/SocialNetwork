from django.utils import timezone
from django.core.cache import cache


class UpdateLastActivityMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(request, 'user') and request.user.is_authenticated():
            cache.set(request.user.username, timezone.now())

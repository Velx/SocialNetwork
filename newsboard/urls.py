from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet
from users.urls import urlpatterns as users_urls

router = SimpleRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
    path('', include(users_urls))
]
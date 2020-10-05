from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, PostAnalyticsViewSet
from users.urls import urlpatterns as users_urls

router = SimpleRouter()
router.register(r'', PostViewSet)

router2 = SimpleRouter()
router2.register(r'', PostAnalyticsViewSet)

urlpatterns = [
    path('posts/', include(router.urls)),
    path('analitics/', include(router2.urls)),
    path('', include(users_urls))
]
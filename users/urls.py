from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, CustomTokenObtainPairView, CustomTokenRefreshView

router = SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls), name='users'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

from datetime import datetime, timedelta
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from .models import Post, LikedBy
from .serializers import PostSerializer, PostAnalyticsSerializer


class PostViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.liked_by.add(request.user)
        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.liked_by.remove(request.user)
        serializer = self.get_serializer(post)
        return Response(serializer.data)


class PostAnalyticsViewSet(ListModelMixin, GenericViewSet):
    queryset = LikedBy.objects.all()
    serializer_class = PostAnalyticsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        date_from = request.query_params.get('date_from', None)
        date_to = request.query_params.get('date_to', None)
        if (date_from and date_to) is not None:
            try:
                date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
                date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
                date_generated = [date_from + timedelta(days=x) for x in range(0, (date_to - date_from).days)]
                result = []
                for date in date_generated:
                    date_likes = {'date': date, 'likes': LikedBy.objects.filter(date=date).count()}
                    result.append(date_likes)
                serializer = PostAnalyticsSerializer(result, many=True)
                return Response(serializer.data)
            except ValueError:
                return Response({"detail": "Wrong query parameters",
                                 "code": "query_params_is_not_valid",
                                 "messages": [{
                                     "message": "Wrong query parameters"}
                                 ]},
                                status=400)
        else:
            return Response({"detail": "Empty query parameters",
                             "code": "query_params_is_empty",
                             "messages": [{
                                 "message": "Please specify query parameters date_from and date_to"}
                             ]},
                            status=400)

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_id', 'author', 'title', 'text', 'creation_date', 'like_count']

    author_id = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    liked = serializers.SerializerMethodField()

    @staticmethod
    def get_liked(obj):
        if serializers.CurrentUserDefault() in obj.liked_by:
            return True
        else:
            return False

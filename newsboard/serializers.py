from rest_framework import serializers
from .models import Post
from .helpers import CurrentUser


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author_id', 'author', 'title', 'text', 'creation_date', 'like_count', 'liked']

    author_id = serializers.HiddenField(default=CurrentUser())
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    liked = serializers.SerializerMethodField()

    def get_liked(self, obj):
        user = self.context['request'].user
        if user.likes.filter(pk=obj.pk).exists():
            return True
        else:
            return False

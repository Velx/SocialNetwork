from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(user_model, on_delete=models.CASCADE, verbose_name='posts')
    title = models.CharField(max_length=70)
    text = models.TextField()
    liked_by = models.ManyToManyField(user_model, related_name='likes')
    creation_date = models.DateTimeField(auto_now=True)

    @property
    def like_count(self):
        return self.liked_by.count

    def __str__(self):
        return self.title

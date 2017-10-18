from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length=75)
    text = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='news', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_comment_count(self):
        # TODO: Fix this function
        return Comment.objects.filter(comment__newPost=self).count()

    def get_pick(self):
        return self.text[:200] + '...'


class Comment(models.Model):
    subject = models.CharField(max_length=50)
    text = models.TextField(max_length=4000)
    post = models.ForeignKey(NewsPost, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='comments')
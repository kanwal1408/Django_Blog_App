from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE) #'on_delete=models.CASCADE' means when a user's account is deleted,all the posts associated with that user is deleted.
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',) # for getting latest posts on top

    def comment_count(self):
        return self.comment_set.all().count()

    def comments(self):
        return self.comment_set.all()

    def __str__(self): # for showing string representation of PostModel inside admin page like 'title'
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content

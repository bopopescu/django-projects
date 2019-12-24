from django.db import models

# Create your models here.
class Post(models.Model):
    url = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField(max_length=200, default='some string')
    def __str__(self):
        return self.body
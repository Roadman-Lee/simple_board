from django.db import models


class Article(models.Model):
    board_id = models.IntegerField(null=False)
    title = models.CharField(max_length=255, null=False)
    article = models.TextField(max_length=1000, null=False)
    password = models.CharField(max_length=255, null=False)
    nickname = models.CharField(max_length=255, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

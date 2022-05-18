from django.db import models


class Comment(models.Model):
    ref_id = models.ForeignKey(
        "Article", related_name="article_comment", on_delete=models.CASCADE
    )
    ref_comment_id = models.ForeignKey(
        "Comment", related_name="ref_comment", on_delete=models.CASCADE
    )
    comment = models.CharField(blank=True, max_length=255)
    nickname = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    comment_lev = models.PositiveSmallIntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

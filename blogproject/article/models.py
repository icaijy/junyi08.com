from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    createTime = models.DateTimeField(default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updateTime',)

    def __str__(self):
        return self.title
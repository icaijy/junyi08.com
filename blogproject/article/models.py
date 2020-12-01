from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
import bs4
import markdown

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = MDTextField(null=True)
    summary = models.TextField(max_length=50, default="")
    createTime = models.DateTimeField(default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updateTime',)

    def __str__(self):
        return self.title



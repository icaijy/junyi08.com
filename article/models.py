from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField

class column(models.Model):
    name = models.CharField(max_length=25)
    createTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Article(models.Model):
    column = models.ForeignKey(
        column,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )
    title = models.CharField(max_length=50)
    content = MDTextField(null=True)
    summary = models.TextField(max_length=50, default="")
    createTime = models.DateTimeField(default=timezone.now)
    updateTime = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    pin = models.BooleanField(default=False)


    def __str__(self):
        return self.title



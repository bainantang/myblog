from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    put_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

# Create your models here.

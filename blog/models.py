from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title

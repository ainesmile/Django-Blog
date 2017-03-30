from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField("article body")
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField('date published')

    class Meta:
        ordering = ("pub_date",)

    def __str__(self):
        return self.title


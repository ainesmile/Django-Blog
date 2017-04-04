from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField("article body")
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments')
    commenter = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.content
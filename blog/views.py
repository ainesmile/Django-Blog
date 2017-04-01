from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Article, Tag

def index(request):
    template_name = 'blog/index.html'
    article_list = Article.objects.all()
    return render(request, template_name, {'article_list': article_list})

def article(request, article_id):
    template_name = 'blog/article.html'
    article = Article.objects.get(pk=article_id)
    return render(request, template_name, {'article': article})

def tag(request, tag_id):
    template_name = 'blog/tag.html'
    tag = Tag.objects.get(pk=tag_id)
    return render(request, template_name, {'tag': tag})
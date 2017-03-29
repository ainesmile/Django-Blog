from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Article

def index(request):
    template_name = 'blog/index.html'
    article_list = Article.objects.all()
    return render(request, template_name, {'article_list': article_list})

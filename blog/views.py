from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Tag
from .forms import CommentForm

def pagination(request, object_list, paginate_by):
    paginator = Paginator(object_list, paginate_by)
    page = request.GET.get('page', 1)
    try:
      result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)
    return result


def index(request):
    template_name = 'blog/index.html'
    article_list = Article.objects.all()
    paginate_by = 1
    articles = pagination(request, article_list, paginate_by)

    return render(request, template_name, {
        'articles': articles,
        'object_list': articles,
    })

def article(request, article_id):
    template_name = 'blog/article.html'
    article = Article.objects.get(pk=article_id)
    return render(request, template_name, {'article': article})

def tag(request, tag_id):
    template_name = 'blog/tag.html'
    tag = Tag.objects.get(pk=tag_id)
    article_list = tag.article_set.all()
    paginate_by = 1
    articles = pagination(request, article_list, paginate_by)

    return render(request, template_name, {
        'tag': tag,
        'articles': articles,
        'object_list': articles
    })

def add_comment(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'blog/add_comment.html', {
        'form': form
    })





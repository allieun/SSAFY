from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required


def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def delete(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()
    return redirect('articles:index')

@login_required
def update(request, article_id):
    # 1. 수정할 게시글을 DB에서 가져오기 (edit, update 함수 공통)
    article = Article.objects.get(pk=article_id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)

    # edit, update 함수 공통
    context = {
        'form': form,
        'article': article, # 어떤 글을 수정하는지 게시글 pk를 URL로 전달하기 위해 필요
    }
    return render(request, 'articles/update.html', context)

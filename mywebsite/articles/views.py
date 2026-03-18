from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from .models import Article


def index(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'articles_index.html', {'articles': articles})


def add(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        author = request.POST.get('author', '').strip()
        if title and content and author:
            Article.objects.create(title=title, content=content, author=author)
            return redirect('articles_index')
    return render(request, 'articles_add.html')

def delete(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return redirect('articles_index')
    return HttpResponseNotAllowed(['POST'])

def edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        author = request.POST.get('author', '').strip()
        if title and content and author:
            article.title = title
            article.content = content
            article.author = author
            article.save()
            return redirect('articles_detail', article_id=article.id)
    return render(request, 'articles_edit.html', {'article': article})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles_detail.html', {'article': article})
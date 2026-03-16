from django.shortcuts import render, redirect
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
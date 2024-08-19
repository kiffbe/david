from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def index(request):
    """article = Article.objects.all()
    article_title = [art.titre for art in article]
    article_title_str = ", ".join(article_title)
    return HttpResponse('Les articles: ' + article_title_str,)"""
    return render(request, 'pagep/index.html', {})


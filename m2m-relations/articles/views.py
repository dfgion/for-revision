from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    objects_list = Article.objects.all().order_by(ordering)
    for article in objects_list:
        print(article.title)
    context = {'object_list': objects_list}
    return render(request, template, context)

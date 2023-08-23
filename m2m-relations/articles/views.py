from django.shortcuts import render

from .models import Article, Tag, Scope

# with open('m2m-relations/articles.json','r','utf8')as file:

def articles_list(request):
    template = 'articles/news.html'
    article_object = Article.objects.all()
    tag = Tag.objects.all()
    scope = Scope.objects.all()
    print(scope)



    context = {'object_list': article_object}
    # context = {'object_list': article_object}
    # context ={}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)
# def tags_list(request):
#     tag = Tag.objects.all()
#     print(tag)
#     return render(request,'')
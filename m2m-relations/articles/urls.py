from django.urls import path

from .views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
    # path('tags/',tag_list,name ='tags_list_url')

]

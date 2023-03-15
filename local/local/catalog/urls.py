from django.urls import path, re_path
from . import views
#127.0.0.1:8000/catalog/book/10

urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'^books/$', views.BookListView.as_view(), name="books"),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name="book-detail"),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name="authors"),
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name="author-detail"),
]

'''
    ^ - начало строки
    $ - конец строки
    \d - любое число (1 символ)
    \w - любая буква (1 символ)
    +  - любое количество символов (1 и более)
    *  - любое количество символов (0 и более)
    () - выражение
    P<a> - переменная а 
'''

from django.shortcuts import render
from django.views import generic

from .models import *


def index(request):
    books_count = Book.objects.all().count()    # select count(*) from Book
    authors_count = Author.objects.all().count()
    books_instances_count = BookInstance.objects.count()
    books_reserved_inst_count = BookInstance.objects.filter(status__exact='r').count()

    visits_count = request.session.get('visits_count', 0)
    request.session['visits_count'] = visits_count + 1

    return render(
        request,
        'index.html',
        context={
            'books_count': books_count,
            'authors_count': authors_count,
            'books_instances_count': books_instances_count,
            'books_reserved_inst_count': books_reserved_inst_count,
            'visits_count': visits_count,
        }
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(generic.DetailView):
    model = Author

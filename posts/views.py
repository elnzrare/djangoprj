from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import book


def home_page(request):
    return HttpResponse("welcome to my library!")


def Book_list(request):
    books = book.objects.all()
    context = {'books': books}
    return render(request, 'posts/book_list.html', context=context)


def book_detail(request, book_id):
    books = book.objects.filter(pk=book_id).first()
    context = {
        'books': books
    }
    return render(request, 'posts/book_detail.html', context=context)


# class based views

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

class BookList(ListView):
    paginate_by = 10
    template_name = "posts/book_list.html"
    context_object_name = "books"
    queryset = book.objects.all()

    def get_queryset(self):
        return self.queryset

class BookDetail(DetailView):
    template_name = "posts/book_detail.html"
    context_object_name = "book"
    queryset = book.objects.all()

    def get_object(self):
        book_id = self.kwargs['book_id']
        return get_object_or_404(
            book.objects.all(),
            pk=book_id
        )




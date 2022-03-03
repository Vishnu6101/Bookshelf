from typing import Any, Dict
from django.shortcuts import redirect, render, get_object_or_404
# from django.http import HttpResponse, Http404
from books.models import Book, Review
from django.views import generic
from django.db.models import QuerySet

from books.form import ReviewForm

# Create your views here.


class BookListView(generic.ListView):
    template_name = 'books/index.html' # default name = <app name>/<model name>_list.html
    context_object_name = 'books' # default name

    def get_queryset(self) -> QuerySet[Book]:
        return Book.objects.all()


class BookDetailView(generic.DeleteView):
    model = Book
    template_name = 'books/show.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # Add reviews to our context
        context['reviews'] = context['book'].review_set.order_by('-createdAt')
        context['authors'] = context['book'].authors.all()
        context['form'] = ReviewForm()
        return context

def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'books' : books}
    context['author'] = author
    return render(request, 'books/author_books.html', context)

def review(request, id):
    if request.user.is_authenticated:
        newReview = Review(book_id=id, userId=request.user)
        form = ReviewForm(request.POST, instance=newReview)
        if form.is_valid():
            form.save()
    return redirect(f"/book/{id}")
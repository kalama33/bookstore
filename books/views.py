from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"    # name of the list of books

class BookDetailView(DetailView):
    model = Book
    template_name = "book_details.html"
    context_object_name = "book"
    
class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "description"]
    template_name = "book_create.html"
    success_url = reverse_lazy("book-list") #

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book-list")  

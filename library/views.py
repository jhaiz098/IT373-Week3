from django.shortcuts import render
from .models import Book, Category

# Create your views here.
def home(request):
    books = Book.objects.all().prefetch_related('category', 'author')
    categories = Category.objects.all()

    return render(request, "home.html", {
        'books': books,
        'categories': categories,
    })
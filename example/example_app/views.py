from django.shortcuts import render
from django.shortcuts import redirect
from .forms import BookForm
from example_app.models import Book

def home(request):
   data = {
       'name': 'John Doe',
       'age': 25,
       'country': 'USA'
   }
   return render(request, 'example_app/home.html', context=data)
# Create your views here.

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'example_app/create_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'example_app/book_list.html', {'books': books})

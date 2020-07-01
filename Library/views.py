from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Issuebook, Patron, Publisher
from .forms import BookForm, CategoryForm, IssuebookForm, PublisherForm, PatronForm


# Create your views here for home page.
def home(request):
    return render(request, 'index.html', {})

# Create your views here for contact page.
def contact(request):
    return render(request, 'contact.html', {})

# Create your views here for books.


def list_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def create_book(request):
    form = BookForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_books')
    return render(request, 'books-form.html', {'form': form})


def update_book(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)

    if form.is_valid():
        form.save()
        return redirect('list_books')

    return render(request, 'books-form.html', {'form': form, 'book': book})


def delete_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('list_books')

    return render(request, 'book-delete-confirm.html', {'book': book})

# Create your views here for categories.


def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def create_category(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_categories')
    return render(request, 'categories-form.html', {'form': form})


def update_category(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect('list_categories')

    return render(request, 'categories-form.html', {'form': form, 'category': category})


def delete_category(request, id):
    category = Category.objects.get(id=id)

    if request.method == 'POST':
        category.delete()
        return redirect('list_categories')

    return render(request, 'category-delete-confirm.html', {'category': category})
# Create your views here for Issuebook.


def issue_book(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = IssuebookForm()
        else:
            issuedbook = Issuebook.objects.get(pk=id)
            form = IssuebookForm(instance=issuedbook)
        return render(request, "issuedbook-form.html", {'form': form})
    else:
        if id == 0:
            form = IssuebookForm(request.POST)
        else:
            issuedbook = Issuebook.objects.get(pk=id)
            form = IssuebookForm(request.POST, instance=issuedbook)
        if form.is_valid():
            form.save()
        return redirect('issuedbooks')


def list_issuebook(request):
    issuedbooks = Issuebook.objects.all()
    return render(request, 'issuedbooks.html', {'issuedbooks': issuedbooks})


def delete_issuebook(request, id):
    issuedbook = Issuebook.objects.get(id=id)

    if request.method == 'POST':
        issuedbook.delete()
        return redirect('issuedbooks')
    return render(request, 'issuedbook-confirm-delete.html', {'issuedbook': issuedbook})


# views for publisher

def list_publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers':publishers})

def create_publisher(request):
    form = PublisherForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_publishers')
    return render(request, 'publishers-form.html', {'form': form})

def update_publisher(request, id):
    publisher = Publisher.objects.get(id=id)
    form = PublisherForm(request.POST or None, instance=publisher)

    if form.is_valid():
        form.save()
        return  redirect('list_publishers')

    return render(request, 'publishers-form.html', {'form': form, 'publisher': publisher})

def delete_publisher(request, id):
    publisher = Publisher.objects.get(id=id)

    if request.method == 'POST':
        publisher.delete()
        return redirect('list_publishers')

    return render(request, 'publisher-delete-confirm.html', {'publisher': publisher})

# Create your views for Patron here.
def list_patrons(request):
    patrons = Patron.objects.all()
    return render(request, 'patrons.html', {'patrons': patrons})

def create_patron(request):
    form = PatronForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_patrons')
    return render(request, 'patrons-form.html', {'form': form})

def update_patron(request, id):
    patron = Patron.objects.get(id=id)
    form = PatronForm(request.POST or None, instance=patron)

    if form.is_valid():
        form.save()
        return  redirect('list_patrons')

    return render(request, 'patrons-form.html', {'form': form, 'patron': patron})

def delete_patron(request, id):
    patron = Patron.objects.get(id=id)

    if request.method == 'POST':
        patron.delete()
        return redirect('list_patrons')

    return render(request, 'patron-delete-confirm.html', {'patron': patron})



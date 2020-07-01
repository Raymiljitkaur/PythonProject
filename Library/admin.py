from django.contrib import admin
from .models import Book, Patron, Category, Publisher

# Register your models here.
admin.site.register(Book)
admin.site.register(Patron)
admin.site.register(Category)
admin.site.register(Publisher)
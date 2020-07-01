from django import forms
from .models import Book, Category, Issuebook, Publisher, Patron


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class PatronForm(forms.ModelForm):
    class Meta:
        model = Patron
        fields = "__all__"

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = "__all__"


class IssuebookForm(forms.ModelForm):
    class Meta:
        model = Issuebook
        fields = ['book', 'patron', 'issuedate', 'expirydate']

    def __init__(self, *args, **kwargs):
        super(IssuebookForm, self).__init__(*args, **kwargs)
        self.fields['book'].empty_label = "Select"
        self.fields['patron'].empty_label = "Select"

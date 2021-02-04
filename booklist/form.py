from django import forms
from .models import Book


class RequestToAddBook(forms.Form):
    title = forms.CharField(required=True)
    author = forms.CharField(required=True)

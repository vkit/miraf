from django import forms
from .models import BookComment, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher','description','price','category_books','status')


# class BookCommentForm(forms.ModelForm):
#     class Meta:
#         model = BookComment
#         fields = ('name', 'email', 'body')

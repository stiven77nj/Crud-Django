from django import forms
from .models import Author
from .models import Book

#Crear formulario
class AuthorForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Author

        #especificar los campos
        fields = [
            'first_name',
            'last_name',
            'photo',
            'birth_date'
        ]

#Crear formulario
class BookForm(forms.ModelForm):

    #metaclase
    class Meta:
        model = Book

        #especificar los campos
        fields = [
            'name',
            'description',
            'year',
            'cost',
            'author'
        ]
from django.forms import ModelForm , TextInput 
from .models import Book 

class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class' : 'form-control',
                # 'style':'color:coral ; width:80px',


            })
        }


       
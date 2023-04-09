from django.shortcuts import render , redirect

from book.forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer

@login_required(login_url='/')
def index(request):  
    user = request.user
    books = Book.objects.filter(user = user)
    
    context = {
        "books" :books,
    }
    return  render(request , 'index.html' , context)

def createBook(request):
    form = Book()
    if request.method == "POST":
        form = Book(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'create.html' , context)



def updateBook(request , pk):
    todo = Book.objects.get(id= pk)
    form = Book(instance=todo)
    if request.method == "POST":
        form = Book(request.POST , instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form": form
    }
    return render(request , 'update.html' , context)



def delete(request , pk):
    todo = Book.objects.get(id=pk)
    Book.delete()
    return redirect('/')

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
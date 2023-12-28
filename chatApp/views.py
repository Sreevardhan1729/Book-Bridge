from django.contrib.auth import login
from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm
from .models import Book

from django.http import HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
import random
# Create your views here.
def frontpage(request):
    return render(request,'chatApp/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()
    return render(request, 'chatApp/signup.html', {'form': form})



def start(request):
    books=Book.objects.all()
    rbooks = get_random_books()
    return render(request,'chatApp/page.html',{'books':books,'rbooks':rbooks})
def add_book(request):
    if request.method=='POST':
        # form = BookForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponse("DONE")
        # else:
        #     print(form.errors)
        username = request.POST.get('username')
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        year_of_publication = request.POST.get('year_of_publication')
        cost = request.POST.get('cost')
        genre = request.POST.get('genre')
        has_image = request.POST.get('has_image')
        state_location = request.POST.get('state_location')
        description = get_book_data(book_name)  # Fixed variable name
        if description=="":
            return render(request,'chatApp/sell.html',{'z':True})
        else:
            book = Book(username=username, book_name=book_name, author_name=author_name, year_of_publication=year_of_publication, cost=cost, genre=genre, has_image=has_image,book_description=description, state_location=state_location)
            book.save()

        return redirect('start')
    return render(request,'chatApp/sell.html')
def sell_book(request):
    return render(request,'chatApp/sell.html')


def get_book_data(book_title):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    api_key = "AIzaSyD_f7nDYJyycuNUEFODxvvXlYJCE2qNpXA"
    params = {
        "q": f"intitle:{book_title}", 
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        items = data.get("items", [])

        if items:
            web_link = items[0]["volumeInfo"].get("previewLink")
            if web_link:
                web_response = requests.get(web_link)
                web_content = web_response.content
                soup = BeautifulSoup(web_content, 'html.parser')
                description = soup.find("meta", attrs={"name": "description"})
                if description:
                    description = description["content"]
                else:
                    description = "No description available"

                return description
            else:
                return ""
        else:
            return ""
    else:
        return "Error: Unable to fetch data from the API"
    
def book_detail(request, book_name, author_name):
    current_book = Book.objects.get(book_name=book_name, author_name=author_name)
    book = get_object_or_404(Book, book_name=book_name, author_name=author_name)
    books = Book.objects.filter(genre=book.genre).exclude(id=current_book.id)
    return render(request,'chatApp/index1.html',{'book':book,'books':books})

def get_random_books():
    # Get all books from the database
    all_books = Book.objects.all()
    
    # Take the first four books from the shuffled list
    random_books = random.sample(list(all_books), 5)
    
    return random_books
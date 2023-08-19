from django.shortcuts import render
from .forms import reviewForm
from .models import Book,Review

# Create your views here.
def review(request):
    form= reviewForm()
    if request.method == 'POST':
        form=reviewForm(request.POST)
        if form.is_valid():
            form.save()
        
    Cnt_model = {'Form': form}
    return render (request,'reviewform.html', Cnt_model)

def index(request): 
    book_list = Book.objects.all()
    Cnt_book={'Book_list':book_list}
    return render(request,'index.html',Cnt_book)

def bookdetail(request,pk):
    book = Book.objects.get(id=pk)
    review=Review.objects.get(id=pk)
    detBook={'detbook':book,
             'revbook':review}


    return render(request,'bookdetail.html',detBook)

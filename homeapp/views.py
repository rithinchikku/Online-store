from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .forms import Bookform
from .models import Book

def createbook(request):
    book=Book.objects.all()
    if request.method=='POST':
        form=Bookform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form=Bookform()
    return render(request,'admin/create.html',{'form':form,'book':book})

def listbook(request):
    book=Book.objects.all()
    paginator=Paginator(book,4)
    page_num=request.GET.get('page')
    try:
        page=paginator.get_page(page_num)
    except EmptyPage:
        page=paginator.page(page_num.num_pages)
    return render(request,'admin/display.html',{'book':book,'page':page})
def detailsview(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,'admin/details.html',{'book':book},)

def updateview(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form =Bookform(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form=Bookform(instance=book)
    return render(request,'admin/update.html',{'form':form})

def deletebook(request,book_id):
    book=Book.objects.get(id=book_id)

    if request.method=='POST':
        book.delete()
        return redirect('display')
    return render(request,'admin/delete.html',{'book':book})


 # downlaod templates view setup

def index(request):
    return render(request,'admin/signin.html')

def search(request):
    query=None

    if 'q' in request.GET:

        query=request.GET.get('q')
        book=Book.objects.filter(Q(title__icontains=query))

    else:
        book=[]
    context={'book':book,'query':query}
    return render(request,'admin/search.html',context)



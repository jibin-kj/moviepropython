from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie1':movie})
    #return HttpResponse("this is movie no %s" % movie_id)
def add_movie(request):
    if request.method=="POST":
        name1=request.POST.get('name',)
        desc1 = request.POST.get('desc', )
        year1 = request.POST.get('year', )
        img1 = request.FILES['img']
        movie=Movie(name=name1,desc=desc1,year=year1,img=img1)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movie1=Movie.objects.get(id=id)
    form1=MovieForm(request.POST or None,request.FILES,instance=movie1)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form1,'movie':movie1})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
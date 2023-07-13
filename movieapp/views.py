from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie

    }
    return render(request, 'index.html', context)


def details(requset, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(requset, "detail.html", {'movie': movie})


def add_movie(requset):
    if requset.method == 'POST':
        name = requset.POST.get('name')
        desc = requset.POST.get('desc')
        year = requset.POST.get('year')
        img = requset.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
    return render(requset, "add.html")


def update(requset, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(requset.POST or None, requset.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(requset, "edit.html", {'form': form, 'movie': movie})


def delete(requset, id):
    if requset.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(requset, "delete.html")

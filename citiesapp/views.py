from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import City, Comment

from .forms import CommentForm

def index(request):
    cities = City.objects.all()

    return render(request, 'cities.html', {'cities': cities})

def get_city(request, id):
    city = City.objects.get(id=id)
    comments = Comment.objects.filter(city=id)

    comments_form = CommentForm()

    return render(request, 'city.html', {'city': city, 'form': comments_form, 'comments': comments})

def create_new_comment(request, id):
    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.city = City.objects.get(id=id)

            new_comment.save()
        
        return redirect('city', id=id)

    else: 
        return redirect('city', id=id)
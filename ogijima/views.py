from django.shortcuts import render
from django.http import HttpResponse
from .models import (
    Work, Blog, Gallery, Notification, Profile, Art, Restaurant, Hotel, Cat
)
from markdown import markdown

# Create your views here.
def top(request):
    return render(request,'top.html')

def aboutus(request):
    return render(request,'aboutus.html')

def works(request):
    return render(request,'works.html')

def work_detail(request):
    return render(request,'work_detail.html')

def reports(request):
    return render(request,'reports.html')

def blog_detail(request, id):
    return render(request,'blog_detail.html')

def profile(request):
    return render(request,'profile.html')

def information(request):
    arts = Art.objects.all()
    restaurants = Restaurant.objects.all()
    hotels = Hotel.objects.all()
    cats = Cat.objects.all()
    params = {
        'arts': arts,
        'restaurants': restaurants,
        'hotels': hotels,
        'cats': cats,
    }
    return render(request,'information.html', params)

def arts(request):
    return render(request,'arts.html')

def restaurants(request):
    return render(request,'restaurants.html')

def hotels(request):
    return render(request,'hotels.html')

def cats(request):
    return render(request,'cats.html')

def gallery(request):
    photos = Gallery.objects.all()
    params = {
        "photos": photos
    }
    return render(request,'gallery.html', params)

def notifications(request):
    return render(request,'notifications.html')

def contact(request):
    return render(request,'contact.html')

def contact_completed(request):
    return render(request,'contact_completed.html')

def sponsor(request):
    return render(request,'sponsor.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')
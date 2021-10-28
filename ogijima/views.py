from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def top(request):
    return render(request,'top.html')

def abouts(request):
    return render(request,'abouts.html')

def works(request):
    return render(request,'works.html')

def work_detail(request):
    return render(request,'work_detail.html')

def reports(request):
    return render(request,'reports.html')

def blog_detail(request):
    return render(request,'blog_detail.html')

def profile(request):
    return render(request,'profile.html')

def information(request):
    return render(request,'information.html')

def arts(request):
    return render(request,'arts.html')

def restaurants(request):
    return render(request,'restaurants.html')

def hotels(request):
    return render(request,'hotels.html')

def cats(request):
    return render(request,'cats.html')

def gallery(request):
    return render(request,'gallery.html')

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
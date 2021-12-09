from django.shortcuts import render, redirect
from django.http import HttpResponse
from ogijima.forms import ContactForm
from .models import *
from markdown import markdown

# Create your views here.
def top(request):
    return render(request,'top.html')

def aboutus(request):
    return render(request,'aboutus.html')

def works(request):
    all_works = Work.objects.all().order_by("-work_start_date")
    today = timezone.now().date()
    now_works = Work.objects.filter(work_start_date__lte=today,work_end_date__gte=today).all()
    if(now_works.count()==0):
        now_works = all_works.filter(work_start_date__lte=today).first()
        if(now_works==None):
            now_works_date = today
        else:
            now_works_date = now_works.work_start_date
        future_works = all_works.filter(work_start_date__gt=now_works_date)
    else:
        future_works = all_works.filter(work_start_date__gt=today)
    past_works = all_works.filter(work_end_date__lt=today)
    params = {
        'now_works':now_works,
        'future_works':future_works,
        'past_works':past_works,
    }
    return render(request,'works.html',params)

def work_detail(request,work_id):
    work = Work.objects.get(pk=work_id)
    work.content = markdown(work.content)
    return render(request,'work_detail.html',{'work':work})

def reports(request):
    blog = Blog.objects.all()
    return render(request,'reports.html',{'blog':blog})

def blog_detail(request,blog_id):
    blog = Blog.object.get(pk=blog_id)
    blog.content = markdown(blog.content)
    return render(request,'blog_detail.html',{'blog':blog})

def profile(request):
    profile = Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})

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
    art = Art.objects.all()
    return render(request,'arts.html',{'art':art})

def restaurants(request):
    restaurant = Restaurant.objects.all()
    return render(request,'restaurants.html',{'restaurant':restaurant})

def hotels(request):
    hotel = Hotel.objects.all()
    return render(request,'hotels.html',{'hotel':hotel})

def cats(request):
    cat = Cat.objects.all()
    return render(request,'cats.html',{'cat':cat})

def gallery(request):
    photos = Gallery.objects.all()
    params = {
        "photos": photos
    }
    return render(request,'gallery.html', params)

def notifications(request):
    notification = Notification.objects.all()
    return render(request,'notifications.html',{'notification':notification})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_completed', email=form.email)
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form': form})

def contact_completed(request):
    return render(request,'contact_completed.html')

def sponsor(request):
    return render(request,'sponsor.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')
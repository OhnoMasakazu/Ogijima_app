from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from ogijima.forms import ContactForm, ApplyForm, ApplicationForm
from .models import *
from markdown import markdown
import re
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def top(request):
    all_works = Work.objects.all().order_by("-work_start_date")
    today = timezone.now().date()
    now_works = Work.objects.filter(work_start_date__lte=today,work_end_date__gte=today).all()
    future_works = all_works.filter(work_start_date__gt=today)
    p = re.compile(r"<[^>]*?>")
    if now_works:
        now_works = now_works.order_by("work_start_date")
        for now_work in now_works:
            now_work.content = p.sub("", markdown(now_work.content))
    if future_works:
        future_works = future_works.order_by("work_start_date")
        future_work = future_works[0]
        future_work.content = p.sub("", markdown(future_work.content))
    else:
        future_work = []
    
    arts = Art.objects.all()
    restaurants = Restaurant.objects.all()
    hotels = Hotel.objects.all()
    cats = Cat.objects.all()

    slideshow_pc = Slideshow_pc.objects.all().order_by("order")
    slideshow_mobile = Slideshow_mobile.objects.all().order_by("order")

    notifications = Notification.objects.all().order_by("-date")[0:5]

    params = {
        'now_works': now_works,
        'future_work': future_work,
        'arts': arts,
        'restaurants': restaurants,
        'hotels': hotels,
        'cats': cats,
        'slideshow_pc': slideshow_pc,
        'slideshow_mobile': slideshow_mobile,
        'notifications': notifications,
    }
    return render(request,'top.html', params)

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
        # future_works = all_works.filter(work_start_date__gt=now_works_date)
    # else:
    #     future_works = all_works.filter(work_start_date__gt=today)
    # past_works = all_works.filter(work_end_date__lt=today)
    now_works = now_works.order_by("work_start_date")
    # future_works = future_works.order_by("work_start_date")[0:5]
    # past_works = past_works.order_by("-work_start_date")[0:5]
    p = re.compile(r"<[^>]*?>")
    for work in now_works:
        work.content = p.sub("", markdown(work.content))
    # for work in future_works:
    #     work.content = p.sub("", markdown(work.content))
    # for work in past_works:
    #     work.content = p.sub("", markdown(work.content))
    params = {
        'now_works':now_works,
        # 'future_works':future_works,
        # 'past_works':past_works,
    }
    return render(request,'works.html',params)

def planed_works(request):
    today = timezone.now().date()
    future_works = Work.objects.all().filter(work_end_date__gt=today)
    future_works = future_works.order_by("work_start_date")
    p = re.compile(r"<[^>]*?>")
    for work in future_works:
        work.content = p.sub("", markdown(work.content))
    # paginator = Paginator(future_works, 10)
    paginator = Paginator(future_works, 5)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'planed_works.html', params)

def held_works(request):
    today = timezone.now().date()
    past_works = Work.objects.all().filter(work_end_date__lt=today)
    past_works = past_works.order_by("-work_start_date")
    p = re.compile(r"<[^>]*?>")
    for work in past_works:
        work.content = p.sub("", markdown(work.content))
    # paginator = Paginator(past_works, 10)
    paginator = Paginator(past_works, 5)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'held_works.html', params)

def work_detail(request,work_id):
    work = Work.objects.get(pk=work_id)
    work.content = markdown(work.content)
    worklist = Work.objects.order_by('work_start_date')
    idx = list(map(lambda x:x.pk, worklist)).index(work_id)
    if idx==0:
        prev_id = -1
    else:
        prev_id = worklist[idx-1].pk
    if idx==len(worklist)-1:
        next_id  = -1
    else:
        next_id = worklist[idx+1].pk
    params = {
        'work':work,
        'prev_id':prev_id,
        'next_id':next_id
    }
    return render(request,'work_detail.html',params)

def reports(request):
    blog = Blog.objects.all().order_by('-date')
    paginator = Paginator(blog, 5)
    # paginator = Paginator(blog, 10)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    p = re.compile(r"<[^>]*?>")
    for blog in pages:
        blog.content = p.sub("", markdown(blog.content))
    params = {
        'pages': pages,
    }
    return render(request,'reports.html', params)

def blog_detail(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    blog.content = markdown(blog.content)
    bloglist = Blog.objects.order_by('date')
    idx = list(map(lambda x:x.pk, bloglist)).index(blog_id)
    if idx==0:
        prev_id = -1
    else:
        prev_id = bloglist[idx-1].pk
    if idx==len(bloglist)-1:
        next_id  = -1
    else:
        next_id = bloglist[idx+1].pk
    params = {
        'blog':blog,
        'prev_id':prev_id,
        'next_id':next_id
    }
    return render(request,'blog_detail.html',params)

def profile(request):
    profile = Profile.objects.all().order_by('order')
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
    art = Art.objects.all().order_by('id')
    paginator = Paginator(art, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'arts.html', params)

def art_detail(request, id):
    art = Art.objects.get(pk=id)
    art.document = markdown(art.document)
    return render(request,'art_detail.html',{'art':art})

def aikien_detail(request):
    model = Contact
    art = Art.objects.get(pk=7)
    art.document = markdown(art.document)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            postdata = Contact(
                name = request.POST['name'],
                mail = request.POST['mail'],
                content = request.POST['content'],
                application_file = request.FILES['application_file'],
                terms_file = request.FILES['terms_file'],
            )
            postdata.save()
            name = request.POST['name']
            email = request.POST['mail']
            text = request.POST['content']
            subject = "【男木島名物倉庫『あいきえん』】アートギャラリーお申込内容の確認"
            message = """※このメールはシステムからの自動返信です。

{name} 様
アートギャラリーのご利用申込いただきありがとうございます。
以下の内容で承りました。ご確認よろしくお願いします。
添付いただいたファイルも添付しておりますので、併せてご確認ください。

━━━━━━□■□　申込内容　□■□━━━━━━
お名前 ： {name}

メールアドレス ： {email}

申込内容：
{text}
━━━━━━━━━━━━━━━━━━━━━━━━━━


担当の者より、数日で返信させていただきますので、今しばらくお待ちくださいませ。


※このメールは送信専用です。このメールにご返信いただいても、お返しすることができませんので、ご了承ください。
""".format(name=name, email=email, text=text)
            from_email = '男木島名物倉庫『あいきえん』お問い合わせ <{email}>'.format(email=settings.EMAIL_HOST_USER)
            recipient_list = ['{email}'.format(email=email)]
            bcc = ['{email}'.format(email=settings.EMAIL_HOST_USER),'ogijima.pj.hp@gmail.com']
            try:
                send_mail = EmailMessage(subject, message, from_email, recipient_list, bcc)
                send_mail.attach_file(Contact.objects.get(pk=postdata.id).application_file.path)
                send_mail.attach_file(Contact.objects.get(pk=postdata.id).terms_file.path)
                send_mail.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")
            return redirect('ogijima:contact_completed',request.POST['mail'])
    else:
        form = ApplicationForm()  
    return render(request,'aikien_detail.html', {'art': art,'form': form})

def restaurants(request):
    restaurant = Restaurant.objects.all().order_by('id')
    paginator = Paginator(restaurant, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'restaurants.html', params)

def restaurant_detail(request, id):
    restaurant = Restaurant.objects.get(pk=id)
    restaurant.document = markdown(restaurant.document)
    restaurant.businessHour = markdown(restaurant.businessHour)
    return render(request,'restaurant_detail.html',{'restaurant':restaurant})

def hotels(request):
    hotel = Hotel.objects.all().order_by('id')
    paginator = Paginator(hotel, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'hotels.html', params)

def hotel_detail(request, id):
    hotel = Hotel.objects.get(pk=id)
    hotel.document = markdown(hotel.document)
    hotel.businessHour = markdown(hotel.businessHour)
    return render(request,'hotel_detail.html',{'hotel':hotel})

def cats(request):
    cat = Cat.objects.all().order_by('id')
    paginator = Paginator(cat, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'cats.html', params)

def cat_detail(request, id):
    cat = Cat.objects.get(pk=id)
    cat.document = markdown(cat.document)
    return render(request,'cat_detail.html',{'cat':cat})

def gallery(request):
    photos = Gallery.objects.all().order_by("-date")
    paginator = Paginator(photos, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'gallery.html', params)

def notifications(request):
    notification = Notification.objects.all()
    paginator = Paginator(notification, 10)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'notifications.html', params)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            email = form.return_email()
            return redirect('ogijima:contact_completed', email)
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form': form})

def contact_completed(request,email):
    return render(request,'contact_completed.html',{'email': email})

def sponsor(request):
    names = Sponsor_name.objects.all().order_by('order')
    banners = Sponsor_banner.objects.all().order_by('order')
    params = {
        'names': names,
        'banners': banners,
    }
    return render(request,'sponsor.html', params)

def privacypolicy(request):
    return render(request,'privacypolicy.html')

# 営業資料用サンプル
def restaurants_sample(request):
    restaurant = Restaurant_sample.objects.all()
    paginator = Paginator(restaurant, 12)
    page = request.GET.get('page', 1)
    try:
        pages = paginator.page(page)
    except PageNotAnInteger:
        pages = paginator.page(1)
    except EmptyPage:
        pages = paginator.page(1)
    params = {
        'pages': pages,
    }
    return render(request,'restaurants_sample.html', params)

def restaurant_detail_sample(request, id):
    restaurant = Restaurant_sample.objects.get(pk=id)
    restaurant.document = markdown(restaurant.document)
    restaurant.businessHour = markdown(restaurant.businessHour)
    return render(request,'restaurant_detail_sample.html',{'restaurant':restaurant})
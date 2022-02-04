from django.db import models
from django.utils import timezone
from markdown import markdown

class Work(models.Model):
    date = models.DateTimeField(default=timezone.now)
    work_start_date = models.DateTimeField()
    work_end_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=300)
    content = models.TextField()
    def __str__(self):
        return self.title

class Blog(models.Model):
    date = models.DateTimeField(default=timezone.now)
    thumbnail = models.CharField(max_length=300)
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return self.title

class Gallery(models.Model):
    date = models.DateTimeField(default=timezone.now)
    photo = models.CharField(max_length=300)
    def __str__(self):
        return str(self.id)

class Notification(models.Model):
    date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    external_link = models.BooleanField(default=False,help_text='クリックした際別タブで開くならTrue')
    def __str__(self):
        return self.content

class Profile(models.Model):
    order = models.FloatField(default=0)
    image = models.CharField(max_length=300)
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=50,blank=True)
    introduction = models.CharField(max_length=300)
    link = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name

class Art(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    apple_maplink = models.CharField(max_length=100,blank=True)
    google_maplink = models.CharField(max_length=100,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    businessHour = models.TextField(max_length=200,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    homepage = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    apple_maplink = models.CharField(max_length=100,blank=True)
    google_maplink = models.CharField(max_length=100,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name

class Hotel(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    businessHour = models.TextField(max_length=200,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    homepage = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    apple_maplink = models.CharField(max_length=100,blank=True)
    google_maplink = models.CharField(max_length=100,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name

class Restaurant_and_hotel(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    businessHour = models.TextField(max_length=200,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    homepage = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    apple_maplink = models.CharField(max_length=100,blank=True)
    google_maplink = models.CharField(max_length=100,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name

class Cat(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name

class Slideshow_pc(models.Model):
    image = models.CharField(max_length=300)
    order = models.FloatField()
    def __str__(self):
        return str(self.order)

class Slideshow_mobile(models.Model):
    image = models.CharField(max_length=300)
    order = models.FloatField()
    def __str__(self):
        return str(self.order)

class Sponsor_name(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=300,blank=True)
    order = models.FloatField()
    def __str__(self):
        return self.name

class Sponsor_banner(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    link = models.CharField(max_length=300,blank=True)
    order = models.FloatField()
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    content = models.TextField(max_length=4000,blank=True)
    application_file = models.FileField(upload_to='media/%Y-%m-%d-%H-%M-%S', blank=True)
    terms_file = models.FileField(upload_to='media/%Y-%m-%d-%H-%M-%S', blank=True)
    # application_file = models.FileField(upload_to='usr/share/nginx/html/media/%Y-%m-%d-%H-%M-%S')
    # terms_file = models.FileField(upload_to='usr/share/nginx/html/media/%Y-%m-%d-%H-%M-%S')

    def __str__(self):
        return self.name

# 営業資料用サンプル
class Restaurant_sample(models.Model):
    thumbnail = models.CharField(max_length=300)
    image = models.CharField(max_length=3000)
    name = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300,blank=True)
    businessHour = models.TextField(max_length=200,blank=True)
    document = models.TextField(max_length=4000,blank=True)
    homepage = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    apple_maplink = models.CharField(max_length=100,blank=True)
    google_maplink = models.CharField(max_length=100,blank=True)
    coordinate_pc_top = models.FloatField()
    coordinate_pc_left = models.FloatField()
    coordinate_mobile_top = models.FloatField()
    coordinate_mobile_left = models.FloatField()
    def __str__(self):
        return self.name
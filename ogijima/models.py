from django.db import models
from django.utils import timezone
from markdown import markdown


# Create your models here.
class Work(models.Model):
    date = models.DateTimeField(default=timezone.now)
    work_start_date = models.DateTimeField()
    work_end_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    sumbnail = models.ImageField(upload_to='images/')
    content = models.TextField()

    def get_markdown_text_as_html(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.text)
    def __str__(self):
        return self.title

class Blog(models.Model):
    date = models.DateTimeField(default=timezone.now)
    sumbnail = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    content = models.TextField()

    def get_markdown_text_as_html(self):
        return markdown(self.text)
    def __str__(self):
        return self.title

class Gallery(models.Model):
    date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='images/')
    def __str__(self):
        return str(self.id)

class Notification(models.Model):
    date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.content

class Profile(models.Model):
    order = models.FloatField(default=0)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=20)
    roll = models.CharField(max_length=50)
    introduction = models.CharField(max_length=300)
    link = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Art(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    coordinate1 = models.FloatField()
    coordinate2 = models.FloatField()
    coordinate3 = models.FloatField()
    coordinate4 = models.FloatField()
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    sumbnail = models.ImageField(upload_to='images/',default="../media/images/profile_default.jpeg")
    image = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    introduction = models.TextField(max_length=300,default="null")
    businessHour = models.TextField(max_length=200,default="null")
    document = models.TextField(max_length=4000,default="null")
    homepage = models.CharField(max_length=100,null=True)
    telephone = models.CharField(max_length=100,null=True)
    instagram = models.CharField(max_length=100,null=True)
    twiter = models.CharField(max_length=100,null=True)
    facebook = models.CharField(max_length=100,null=True)
    coordinate1 = models.FloatField()
    coordinate2 = models.FloatField()
    coordinate3 = models.FloatField()
    coordinate4 = models.FloatField()
    def get_markdown_text_as_html(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.text)
    def __str__(self):
        return self.name

class Hotel(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    link = models.CharField(max_length=100,null=True)
    coordinate1 = models.FloatField()
    coordinate2 = models.FloatField()
    coordinate3 = models.FloatField()
    coordinate4 = models.FloatField()
    def __str__(self):
        return self.name

class Cat(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=100)
    coordinate1 = models.FloatField()
    coordinate2 = models.FloatField()
    coordinate3 = models.FloatField()
    coordinate4 = models.FloatField()
    def __str__(self):
        return self.name


class Restaurant_sample(models.Model):
    sumbnail = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    name = models.CharField(max_length=50)
    introduction = models.TextField(max_length=300,default="null")
    businessHour = models.TextField(max_length=200,default="null")
    document = models.TextField(max_length=4000,blank=True)
    homepage = models.CharField(max_length=100,blank=True)
    telephone = models.CharField(max_length=100,blank=True)
    instagram = models.CharField(max_length=100,blank=True)
    twitter = models.CharField(max_length=100,blank=True)
    facebook = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    maplink = models.CharField(max_length=100,blank=True)
    coordinate1 = models.FloatField()
    coordinate2 = models.FloatField()
    coordinate3 = models.FloatField()
    coordinate4 = models.FloatField()
    def get_markdown_text_as_html(self):
        """MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        return markdown(self.text)
    def __str__(self):
        return self.name
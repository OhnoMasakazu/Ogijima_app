from django.contrib import admin
from django.urls import path
from .import views

app_name = 'ogijima'
urlpatterns = [
    path('',views.top,name="top"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('works',views.works,name="works"),
    path('planed_works',views.planed_works,name="planed_works"),
    path('held_works',views.held_works,name="held_works"),
    path('work_detail/<int:work_id>',views.work_detail,name="work_detail"),
    path('reports',views.reports,name="reports"),
    path('blog_detail/<int:blog_id>',views.blog_detail,name="blog_detail"),
    path('profile',views.profile,name="profile"),
    path('information',views.information,name="information"),
    path('arts',views.arts,name="arts"),
    path('art_detail/<int:id>',views.art_detail,name="art_detail"),
    path('restaurants',views.restaurants,name="restaurants"),
    path('restaurant_detail/<int:id>',views.restaurant_detail,name="restaurant_detail"),
    path('hotels',views.hotels,name="hotels"),
    path('hotel_detail/<int:id>',views.hotel_detail,name="hotel_detail"),
    path('restaurant_and_hotel_detail/<int:id>',views.restaurant_and_hotel_detail,name="restaurant_and_hotel_detail"),
    path('cats',views.cats,name="cats"),
    path('cat_detail/<int:id>',views.cat_detail,name="cat_detail"),
    path('aikien_service',views.aikien_service,name="aikien_service"),
    path('gallery',views.gallery,name="gallery"),
    path('notifications',views.notifications,name="notifications"),
    path('contact',views.contact,name="contact"),
    path('contact_completed/<str:email>',views.contact_completed,name="contact_completed"),
    path('sponsor',views.sponsor,name="sponsor"),
    path('privacypolicy',views.privacypolicy,name="privacypolicy"),

    # 営業資料用サンプル
    path('restaurants_sample',views.restaurants_sample,name="restaurants_sample"),
    path('restaurant_detail_sample/<int:id>',views.restaurant_detail_sample,name="restaurant_detail_sample"),
]
"""ogijima_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include, re_path
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from .models import *

class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = "daily"

    def items(self):
        return [
            "top",
            "aboutus",
            "works",
            "planed_works",
            "held_works",
            "reports",
            "profile",
            "information",
            "arts",
            "restaurants",
            "hotels",
            "cats",
            "gallery",
            "notifications",
            "contact",
            "sponsor",
            "privacypolicy",
        ]

    def location(self, obj):
        return reverse(obj)

class WorkSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Work.objects.order_by("-date")

    def location(self, obj):
        return reverse(obj)

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Blog.objects.order_by("-date")

    def location(self, obj):
        return reverse(obj)

sitemaps = {
    'static': StaticSitemap,
    'work': WorkSitemap,
    'blog': BlogSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")),
    path('',include('ogijima.urls',namespace='ogijima')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
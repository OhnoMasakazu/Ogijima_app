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
from django.urls import path, include, re_path, reverse
# from django.conf.urls import url
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from ogijima.models import *
from django.views.generic import TemplateView
from django.shortcuts import resolve_url

class StaticSitemap(Sitemap):
    priority = 0.6
    changefreq = "never"

    def items(self):
        return [
            "ogijima:top",
            "ogijima:aboutus",
            "ogijima:works",
            "ogijima:planed_works",
            "ogijima:held_works",
            "ogijima:reports",
            "ogijima:profile",
            "ogijima:information",
            "ogijima:arts",
            "ogijima:restaurants",
            "ogijima:hotels",
            "ogijima:cats",
            "ogijima:gallery",
            "ogijima:notifications",
            "ogijima:contact",
            "ogijima:sponsor",
            "ogijima:privacypolicy",
        ]

    def location(self, obj):
        return reverse(obj)

class WorkSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Work.objects.order_by("-date")

    def location(self, obj):
        return resolve_url('ogijima:work_detail', work_id=obj.pk)

class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Blog.objects.order_by("-date")

    def location(self, obj):
        return resolve_url('ogijima:blog_detail', blog_id=obj.pk)

sitemaps = {
    'static': StaticSitemap,
    'work': WorkSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},  name='sitemap'),
    path('',include('ogijima.urls',namespace='ogijima')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # re_path(r'^robots\.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django-sitemap'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]
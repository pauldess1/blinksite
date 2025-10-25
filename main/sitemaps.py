from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'contact', 'particuliers', 'pros']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        priorities = {
            'home': 1.0,
            'about': 0.8,
            'contact': 0.6,
            'particuliers': 0.7,
            'pros': 0.7,
        }
        return priorities.get(item, 0.5)


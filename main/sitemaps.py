from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    protocol = "https"

    def items(self):
        # Liste des noms des vues statiques à inclure dans le sitemap
        return [
            'home',
            'how_it_works',
            'offers',
            'temoignages',
            'contact',
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        # On peut donner une priorité différente selon la page
        priorities = {
            'home': 1.0,
            'how_it_works': 0.8,
            'offers': 0.8,
            'temoignages': 0.6,
            'contact': 0.6,
        }
        return priorities.get(item, 0.5)
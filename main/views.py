from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    Page d'accueil BlinkSite avec Hero et Packs.
    """
    return render(request, 'main/home.html')

def how_it_works(request):
    """
    Section expliquant le fonctionnement.
    """
    return render(request, 'main/how_it_works_page.html')

def offers(request):
    """
    Page pack Starter.
    """
    return render(request, 'main/offers.html')

def temoignages(request):
    return render(request, 'main/temoignages.html')

def contact(request):
    """
    Page Contact.
    """
    return render(request, 'main/contact.html')

def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Disallow: /*?*\n"
        "Sitemap: https://blinksite.fr/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")

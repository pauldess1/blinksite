from django.shortcuts import render

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

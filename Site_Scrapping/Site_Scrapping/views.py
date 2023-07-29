from difflib import SequenceMatcher
import json
from django.db.models import Q

from django.shortcuts import render
import ast
from django.core.paginator import Paginator
from SiteScrappingApp.models import Resultat

def similar(a, b):
    if not a or not b:  # Vérifier si les chaînes de caractères sont vides (None)
        return 0.0  
    return SequenceMatcher(None, a, b).ratio()


def index(request):
    all_products = Resultat.objects.all()
    products_per_page = 20

    # Gestion de la recherche
    search_query = request.GET.get('q')
    if search_query:
        all_products = all_products.filter(Q(designation__icontains=search_query) | Q(site__icontains=search_query))

    # Réappliquer la pagination sur les résultats filtrés/triés
    paginator = Paginator(all_products, products_per_page)
    page_number = request.GET.get('page')
    products_for_page = paginator.get_page(page_number)

    return render(request, 'index.html', {'products': products_for_page, 'search_query': search_query})

def jewellery(request):
    seuil_similarite = 0.8  # Le seuil de similarité souhaité 
    
    data = request.GET.get("data", '')
    # Récupérer toutes les données de votre modèle
    toutes_les_donnees = Resultat.objects.all()
    
    # Utiliser une liste pour stocker les données similaires trouvées
    donnees_similaires = []
    
    # Parcourir toutes les données pour trouver celles dont la désignation est similaire
    for donnee in toutes_les_donnees:
        ratio_similarite = similar(donnee.designation, data)
        if ratio_similarite >= seuil_similarite:
            donnees_similaires.append(donnee)
    
    # Vous pouvez maintenant utiliser les données similaires dans votre template ou faire d'autres opérations
    
    return render(request, "jewellery.html", context={"datas": donnees_similaires})



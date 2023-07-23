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
    with open(r"C:\Users\bassi\OneDrive\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
        data = json.load(file)
    return render(request, "index.html", context={'datas' : data})


def jewellery(request):
    seuil_similarite = 0.8  # Le seuil de similarité souhaité (60% dans votre cas)
    
    data = request.GET.get("data", '')
    data_json = ast.literal_eval(data)
    return render(request, "jewellery.html", context={'data': data_json})

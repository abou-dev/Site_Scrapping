import json

from django.shortcuts import render
import ast

from SiteScrappingApp.models import Resultat

def index(request):
    # with open(r"C:\Users\bassi\OneDrive\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
    #         data = json.load(file)
    produits = Resultat.objects.all()
    return render(request, "index.html", context={'datas': produits})

def jewellery(request):
    data = request.GET.get("data", '')
    produit = Resultat.objects.get(designation = data)
    # data_json = ast.literal_eval(data)
    return render(request, "jewellery.html", context={'data': produit})


def electronic(request):
    return render(request, "electronic.html",)
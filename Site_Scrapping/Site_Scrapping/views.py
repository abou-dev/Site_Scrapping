import json

from django.shortcuts import render

def index(request):
    with open(r"C:\Users\bassi\OneDrive\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
        data = json.load(file)
    return render(request, "index.html", context={'datas' : data})

def electronic(request):
    return render(request, "electronic.html",)

def jewellery(request):
    data = request.GET.get('data', '')
    return render(request, "jewellery.html",  context={'data': data},)
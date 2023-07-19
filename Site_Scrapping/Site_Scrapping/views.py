import json

from django.shortcuts import render
import ast

from Site_Scrapping.utils import get_db_handle


def index(request):
<<<<<<< Updated upstream
    with open(r"C:\Users\bassi\OneDrive\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
        data = json.load(file)
=======
   # with open(r"C:\Users\moussa.sow\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
     #   data = json.load(file)

    data = get_db_handle('resultat_db', 'localhost', 27017, 'user', '')
>>>>>>> Stashed changes
    return render(request, "index.html", context={'datas' : data})

def electronic(request):
    return render(request, "electronic.html",)

def jewellery(request):
    data = request.GET.get("data", '')
    data_json = ast.literal_eval(data)
    return render(request, "jewellery.html", context={'data': data_json})

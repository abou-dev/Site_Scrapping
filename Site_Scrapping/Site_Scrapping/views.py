import json

from django.shortcuts import render
import ast


def index(request):
    with open(r"C:\Users\moussa.sow\Documents\GitHub\Site_Scrapping\Site_Scrapping\Site_Scrapping\data\jumia.json", 'r') as file:
        data = json.load(file)
    return render(request, "index.html", context={'datas' : data})

def electronic(request):
    return render(request, "electronic.html",)

def jewellery(request):
    data = request.GET.get("data", '')
    data_json = ast.literal_eval(data)
    return render(request, "jewellery.html", context={'data': data_json})
def fashion(request):
    return render(request,"fashion.html",)

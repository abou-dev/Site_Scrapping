from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def electronic(request):
    return render(request, "electronic.html")

def jewellery(request):
    return render(request, "jewellery.html")
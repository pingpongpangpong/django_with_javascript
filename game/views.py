from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "public/index.html")

def font(request):
    return render(request, "public/DungGeunMo.json")
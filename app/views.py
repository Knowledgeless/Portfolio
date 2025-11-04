from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "html/home.html")


def graphics(request):
    return render(request, "html/graphics.html")

def projects(request):
    return render(request, "html/projects.html")

def contact(request):
    return render(request, "html/contact.html")

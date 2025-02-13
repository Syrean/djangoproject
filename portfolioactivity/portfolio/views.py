from django.shortcuts import render

def index(request): 
    return render(request, "pages/index.html")
def portf(request): 
    return render(request, "pages/portfolio.html")
def cont(request): 
    return render(request, "pages/contact.html")

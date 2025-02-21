from django.shortcuts import render

def index(request): 
    return render(request, "pages/index.html")
def portf(request): 
    return render(request, "pages/portfolio.html")
def cont(request): 
    return render(request, "pages/contact.html")
def report(request): 
    return render(request, "pages/report.html")
def settings(request): 
    return render(request, "pages/settings.html")
def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
        ]
    return render(request, "pages/dashboard.html", context={"data": data})
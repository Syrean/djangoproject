from django.urls import path 
from .views import index 
from .views import portf 
from .views import cont 

app_name = "portfolio" 

urlpatterns = [ 
    path('', index, name='index'), 
    path('portfolio/', portf, name='portf'), 
    path('contacts/', cont, name='cont'), 
]
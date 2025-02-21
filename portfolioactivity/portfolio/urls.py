from django.urls import path 
from .views import index 
from .views import portf 
from .views import cont 
from .views import dashboard 
from .views import report
from .views import settings

app_name = "portfolio" 

urlpatterns = [ 
    path('', index, name='index'), 
    path('portfolio/', portf, name='portf'), 
    path('contacts/', cont, name='cont'), 
    path('dashboard/', dashboard, name='dashboard'),
    path('report/', report, name='report'),
    path('settings/', settings, name='settings')
]
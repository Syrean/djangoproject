from django.urls import path
from .views import create_item, remove_item, retrieve_item, retrieve_items, modify_item

app_name = "items"

urlpatterns = [
    path('', retrieve_items, name='retrieve_items'),
    path('<int:item_id>/', retrieve_item, name='retrieve_item'),
    path('add/', create_item, name='create_item'),
    path('update/<int:item_id>/', modify_item, name='modify_item'),
    path('delete/<int:item_id>/', remove_item, name='remove_item'),
]
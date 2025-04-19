from django.urls import path
from .views import document_list_view, delete_item_view

app_name = 'documents'

urlpatterns = [
    path('', document_list_view, name='list'),
    path('delete/<int:item_id>/', delete_item_view, name='delete'),
]

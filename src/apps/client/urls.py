from django.urls import path
from . import views


app_name = 'client'

urlpatterns = [
    path('admin/', views.admin_view, name='admin'),
    path('search/', views.search_view, name='search'),
    path('delete/<int:contact_id>', views.delete_view, name='delete'),
    path('export/', views.export_view, name='export'),
]
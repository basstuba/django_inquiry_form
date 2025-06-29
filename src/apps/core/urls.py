from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.top_view, name='top'),
    path('confirm/', views.confirm_view, name='confirm'),
    path('thanks/', views.thanks_view, name='thanks'),
]
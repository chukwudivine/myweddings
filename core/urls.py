from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.getDataPage, name='data'),
    path('logic/', views.logic, name='logic'),
]

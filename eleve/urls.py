from unicodedata import name
from django import views
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='acceuil'),
    path('ajout/',views.ajouter,name='ajout'),
    path('modif/<str:pk>',views.modifier_eleve,name='modif'),
    path('supprimer/<str:pk>',views.supprimer_eleve,name='supprimer'),
    path('search/',views.Eleve_filter,name='search')
]
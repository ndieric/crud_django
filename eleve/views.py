from audioop import reverse
from multiprocessing import context
from pyexpat import model
import re
from urllib import request
from urllib.parse import urlencode
from django.http import HttpResponse
from django.shortcuts import render
import eleve
from eleve.filters import Eleve_filter

from eleve.models import Eleve
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import EleveForm

# Create your views here.

def home(request):
    eleve=Eleve.objects.all()
    context={'eleves':eleve}
    return render(request,'Eleve/Acceuil.html',context)

############################################ methode d enregistrer un eleve
def ajouter(request):
    form=EleveForm()
    if request.method=='POST':
        form=EleveForm(request.POST)
        if form.is_valid():
            form.save()      
            return redirect('/')        
    return render(request,'Eleve/ajout.html',{'form':form})
############################### methode de modifier un eleve ###################################

def modifier_eleve(request,pk):
    eleve=Eleve.objects.get(id=pk)
    form=EleveForm(instance=eleve)
    if request.method=='POST':
        form=EleveForm(request.POST,instance=eleve)
        if form.is_valid():
            form.save()      
            return redirect('/')        
    return render(request,'Eleve/ajout.html',{'form':form})
  ######################################## methode de supprimer un eleve ###################################  
def supprimer_eleve(request,pk):
    eleve=Eleve.objects.get(id=pk)
    if request.method=='POST':
        eleve.delete()
        return redirect('/')
    return render(request,'eleve/supp.html',{'form':eleve})


############################ methode de filtrer les eleves ###########################

def List_eleve(request,pk):
    eleve = Eleve.objects.get(id=pk)
    elev = eleve.eleve_set.all()
    eleve_total=elev.count()
    myfilter=Eleve_filter(request.GET,queryset=elev)
    elev=myfilter.qs
    return render(request,'Eleve/list_eleve.html',{'eleve':eleve,'eleve_total':eleve_total,'myfilter':myfilter})
    
    
    
    
    
    
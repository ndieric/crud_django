from multiprocessing import context
from pyexpat import model
import re
from django.http import HttpResponse
from django.shortcuts import render
import eleve

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
def ajouter(request):
    form=EleveForm()
    if request.method=='POST':
        form=EleveForm(request.POST)
        if form.is_valid():
            form.save()      
            return redirect('/')        
    return render(request,'Eleve/ajout.html',{'form':form})

def modifier_eleve(request,pk):
    eleve=Eleve.objects.get(id=pk)
    form=EleveForm(instance=eleve)
    if request.method=='POST':
        form=EleveForm(request.POST,instance=eleve)
        if form.is_valid():
            form.save()      
            return redirect('/')        
    return render(request,'Eleve/ajout.html',{'form':form})
    
def supprimer_eleve(request,pk):
    eleve=Eleve.objects.get(id=pk)
    if request.method=='POST':
        eleve.delete()
        return redirect('/')
    return render(request,'eleve/supp.html',{'form':eleve})
    
    
    
    
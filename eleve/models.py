from datetime import datetime
from django.db import models

# Create your models here.

class Eleve(models.Model):
    TYPEGENRE=(('Masculin','Masculin'),('Feminin','Feminin'))
    nom=models.CharField(max_length=200,null=True)
    prenom=models.CharField(max_length=200,null=True)
    genre=models.CharField(max_length=200,null=True,choices=TYPEGENRE)
    date_naissance=models.DateTimeField(max_length=200,null=True)
    
    
    def __str__(self):
        return self.nom
    
    

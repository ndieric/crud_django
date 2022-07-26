from dataclasses import fields
from pyexpat import model
import django_filters
from .models import Eleve


class Eleve_filter(django_filters.FilterSet):
    class Meta:
        model=Eleve
        fields='__all__'
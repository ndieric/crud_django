from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('eleve.urls')),
    path('ajout/',include('eleve.urls'))
]

from django.urls import path
from MiFamilia.views import ver_familiar, crear_familiar

urlpatterns = [
    path('crear/', crear_familiar),
    path('ver/', ver_familiar),
]

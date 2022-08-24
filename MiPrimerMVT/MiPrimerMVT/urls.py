from django.contrib import admin
from django.urls import path
from MiFamilia.views import ver_familiar
from MiFamilia.views import crear_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear/', crear_familiar),
    path('ver/', ver_familiar),
]


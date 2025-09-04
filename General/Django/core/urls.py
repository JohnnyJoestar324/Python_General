from django.urls import path

from core.views import receta, contacto

urlpatterns = [
    path('', receta, name='receta'),
    path('', contacto , name='contacto'),
]

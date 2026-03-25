from django.urls import path

from .views import obtener_agregar_items,  modificar_eliminar_item
urlpatterns= [
    path('items/', obtener_agregar_items, name='obtener_agregar_items'),
    path('items/<int:id>/', modificar_eliminar_item),
]
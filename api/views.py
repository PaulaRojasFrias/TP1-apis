from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

items = [{"id": 1, "nombre": "Laptop"},
         {"id": 2, "nombre": "Telefono"},
         {"id": 3, "nombre": "Auriculares"}]


# GET y POST
@csrf_exempt
def obtener_agregar_items(request):
    if request.method == 'GET':
        return JsonResponse(items, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_item = {"id": len(items) + 1, "nombre": data.get("nombre", "Sin nombre")}
            items.append(nuevo_item)
            return JsonResponse(nuevo_item, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)


# PUT y DELETE
@csrf_exempt
def modificar_eliminar_item(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)

            for item in items:
                if item["id"] == id:
                    item["nombre"] = data.get("nombre", item["nombre"])
                    return JsonResponse(item)

            return JsonResponse({"error": "Item no encontrado"}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    elif request.method == 'DELETE':
        for item in items:
            if item["id"] == id:
                items.remove(item)
                return JsonResponse({"mensaje": "Item eliminado"})

        return JsonResponse({"error": "Item no encontrado"}, status=404)

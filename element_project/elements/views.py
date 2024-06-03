from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Element
import json


@csrf_exempt
def element_list(request):
    if request.method == 'GET':
        elements = Element.objects.all()
        data = [
            {
                'id': element.id,
                'name': element.name,
                'description': element.description,
                'created_at': element.created_at
            }
            for element in elements
        ]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        element = Element.objects.create(name=data['name'], description=data['description'])
        return JsonResponse(
            {
                'id': element.id,
                'name': element.name,
                'description': element.description,
                'created_at': element.created_at
            }, 
            status=201
        )
        
@csrf_exempt
def element_detail(request, pk):
    try:
        element = Element.objects.get(pk=pk)
    except Element.DoesNotExist:
        return JsonResponse({'error': 'Element not found'}, status=404)
    
    if request.method == 'GET':
        data = [
        {
            'id': element.id,
            'name': element.name,
            'description': element.description,
            'created_at': element.created_at
        }
        ]
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        element.name = data['name']
        element.description = data['description']
        element.save()
        return JsonResponse(
            {
                'id': element.id,
                'name': element.name,
                'description': element.description,
                'created_at': element.created_at
            }
        )
    
    elif request.method == 'DELETE':
        element.delete()
        return JsonResponse({'message': 'Element deleted successfully'}, status=204)

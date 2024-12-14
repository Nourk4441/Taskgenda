from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = list(Task.objects.values())
        return JsonResponse({'tasks': tasks}, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            title=data.get('title'),
            completed=data.get('completed', False)
        )
        return JsonResponse({'task': {'id': task.id, 'title': task.title}}, status=201)



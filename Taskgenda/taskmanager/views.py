from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

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



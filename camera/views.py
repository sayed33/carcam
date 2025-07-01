from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import CarCapture
from django.views.decorators.csrf import csrf_exempt
import base64
from datetime import datetime
import os
from django.core.files.base import ContentFile
from django.contrib.auth.models import User


@csrf_exempt
def camera_page(request):
    if request.method == 'POST':
        car_type = request.POST.get('car_type')
        car_number = request.POST.get('car_number')
        images = request.FILES.getlist('images[]')

        for img in images:
            CarCapture.objects.create(image=img, car_type=car_type, car_number=car_number)

        return JsonResponse({'status': 'success'})

    return render(request, 'camera/capture.html')
def create_admin_user(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        return HttpResponse("Superuser created")
    return HttpResponse("Superuser already exists")

from django.contrib import admin
from .models import CarCapture
from django.utils.html import format_html

@admin.register(CarCapture)
class CarCaptureAdmin(admin.ModelAdmin):
    list_display = ['id', 'car_type', 'car_number', 'timestamp', 'thumbnail']
    readonly_fields = ['timestamp', 'thumbnail']
    search_fields = ['car_type', 'car_number']
    list_filter = ['timestamp', 'car_type']

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius:8px;" />', obj.image.url)
        return "-"
    thumbnail.short_description = 'الصورة'

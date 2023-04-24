from django.contrib import admin

from recognize.models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'objects_detected', 'timestamp']
    fields = ['image', 'objects_detected', 'timestamp']
from django.contrib import admin
from .models import Header, Footer, Feature, List, You, Pric, Text, Image, Gamepad, Uchdi, Face
# Register your models here.
@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'status']
    list_filter = ['date']
    prepopulated_fields = {'slug':('name',)}
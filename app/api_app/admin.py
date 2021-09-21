from django.contrib import admin
from .models import Number


@admin.register(Number)
class NumberAdmin(admin.ModelAdmin):
    list_display = ('numbers', )

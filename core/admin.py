from django.contrib import admin
from .models import FormName, Field, FormData
from django.db.models.query import QuerySet
from ipywidgets import *
import json
from django.utils.safestring import mark_safe
import re

admin.site.register(FormName)
admin.site.register(Field)

class FormDataAdmin(admin.ModelAdmin):
    list_display = ['formname','value']

admin.site.register(FormData,FormDataAdmin)


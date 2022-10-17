from django.contrib import admin
from .models import FormName, Field, FormData
from django.db.models.query import QuerySet
from ipywidgets import *
import json

admin.site.register(FormName)
admin.site.register(Field)

class DynamicColumn():

    def __init__(self, qs:QuerySet):
        self.qs = qs
        for k in qs:
            formname = FormName.objects.get(id=k.formname_id)
            for k, v in k.value.items():
                self.__name__ = "First Name"

    def __call__(self, widget:Widget) -> str:
        return len(self.qs)


class FormDataAdmin(admin.ModelAdmin):
    list_display = ()

    def get_list_display(self, request):
        qs = self.get_queryset(request)
        dc = DynamicColumn(qs)
        out = list(self.list_display)
        out.append(dc)  # Add multiple different instances if you want
        return out

admin.site.register(FormData,FormDataAdmin)


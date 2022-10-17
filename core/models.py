from django.db import models
import jsonfield
from django.utils.text import slugify

class FormName(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

class Field(models.Model):
    type = jsonfield.JSONField()
    label = jsonfield.JSONField()
    more_field = jsonfield.JSONField()
    field_type = models.CharField(max_length=100,null=True)
    formname = models.ForeignKey(FormName, on_delete=models.CASCADE)

    def __str__(self):
        return self.formname.name

class FormData(models.Model):
    value = jsonfield.JSONField()
    formname = models.ForeignKey(FormName, on_delete=models.CASCADE)

    def __str__(self):
        return self.formname.name
from django.db import models

from . import constants
# Create your models here.

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if kwargs.get("update_fields"):
            update_fields = list(kwargs.get("update_fields"))
            if "modified_on" not in update_fields:
                update_fields.append("modified_on")
            kwargs["update_fields"] = update_fields
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Company(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    contact = models.BigIntegerField()
    about = models.TextField()

    class Meta:
        abstract = True


class Document(BaseModel):
    name = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=50, choices=constants.Document.choices)
    file = models.FileField(upload_to='document/')

    class Meta:
        abstract = True

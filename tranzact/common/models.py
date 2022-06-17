from django.db import models

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
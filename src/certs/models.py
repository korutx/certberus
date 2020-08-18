import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """
    Base Model for the solution. This model defines the common attributes as a design constraint
        . Id field must be an UUID
        . Every model must have a creator FK referencing the current authenticated user 
    """
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    creator = models.ForeignKey(User, on_delete = models.PROTECT)
    
    class Meta:
        abstract = True

class Project(BaseModel):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 2000)
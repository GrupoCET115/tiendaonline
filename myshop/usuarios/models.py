from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CodigoAutenticacion(models.Model):
    usuario =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    codigo = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    creado = models.DateTimeField(auto_now_add=True)



from django.db import models

# Create your models here.
class LarreaMuñozGit (models.Model):
    curso = models.TextField()
    nombres = models.TextField()
    apellidos = models.TextField()
    profesor = models.TextField()
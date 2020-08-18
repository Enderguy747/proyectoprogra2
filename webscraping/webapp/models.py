from django.db import models

# Create your models here.
class Citas(models.Model):
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    tag = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'citas'

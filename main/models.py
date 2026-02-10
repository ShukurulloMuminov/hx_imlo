from django.db import models
from django.contrib import admin
from django.db.models import ForeignKey
from django.db.models.fields import CharField


class Togri(models.Model):
    soz = CharField(max_length=50)

    def __str__(self):
        return self.soz

    class Meta:
        verbose_name = "To'g'ri so'z"
        verbose_name_plural = "To'g'ri so'zlar"

class Notogri(models.Model):
    soz = CharField(max_length=50)
    togri = ForeignKey(Togri, on_delete=models.CASCADE)


    def __str__(self):
        return self.soz


    class Meta:
        verbose_name = "Noto'g'ri so'z"
        verbose_name_plural = "Noto'g'ri so'zlar"
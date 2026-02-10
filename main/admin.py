from django.contrib import admin
from django.contrib.admin import StackedInline

from main.models import *

class NotogriInline(StackedInline):
    model = Notogri
    extra = 1


class TogriAdmin(admin.ModelAdmin):
    inlines = [NotogriInline]

admin.site.register(Togri, TogriAdmin)
admin.site.register(Notogri)


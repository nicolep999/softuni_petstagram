from django.contrib import admin

from pets.models import Pet


@admin.register(Pet)
class PetModelAdmin(admin.ModelAdmin):
    pass

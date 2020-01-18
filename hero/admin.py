from django.contrib import admin

from .models import Hero

class HeroAdmin(admin.ModelAdmin):
    list_display = ("name", "alias")

admin.site.register(Hero, HeroAdmin)
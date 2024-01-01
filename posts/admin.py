from django.contrib import admin
from . import models

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "created_at",
        "updated_at",
    ]

admin.site.register(models.Post, PostAdmin)

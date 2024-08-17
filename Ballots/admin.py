from django.contrib import admin

from .models import Topics, Comment, Ballots

# Register your models here.

admin.site.register(Topics)

admin.site.register(Comment)

admin.site.register(Ballots)
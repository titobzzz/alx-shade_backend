from django.contrib import admin

from .models import  *

# Register your models here.

admin.site.register(Topics)

admin.site.register(Comment)

admin.site.register(Tabs)

admin.site.register(TabMedia)
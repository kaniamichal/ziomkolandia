from django.contrib import admin

from .models import Kindergarten, Camp, DayCamp

admin.site.register(Kindergarten),
admin.site.register(Camp),
admin.site.register(DayCamp),

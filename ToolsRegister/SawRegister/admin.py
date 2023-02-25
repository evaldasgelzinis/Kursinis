from django.contrib import admin
from .models import JobCenter, Saw, SawName

admin.site.register(JobCenter)
admin.site.register(SawName)
admin.site.register(Saw)


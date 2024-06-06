from django.contrib import admin
from .models import profile,skills,Inbox

# Register your models here.
admin.site.register(profile)
admin.site.register(skills)
admin.site.register(Inbox)
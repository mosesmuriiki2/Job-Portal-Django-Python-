from django.contrib import admin

# Register your models here.
from .models import Job, Applicants, Selected

admin.site.register(Job)
admin.site.register(Selected)
admin.site.register(Applicants)
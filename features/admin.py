from django.contrib import admin
from .models import *

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass

@admin.register(Cause)
class CauseAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(gallery)
class galleryAdmin(admin.ModelAdmin):
    pass

@admin.register(events)
class eventsAdmin(admin.ModelAdmin):
    pass

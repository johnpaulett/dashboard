from django.contrib import admin
from travel.models import ScheduledDeparture

class ScheduledDepartureAdmin(admin.ModelAdmin):
    list_display = ('time', 'direction')
admin.site.register(ScheduledDeparture, ScheduledDepartureAdmin)

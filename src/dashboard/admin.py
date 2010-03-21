from django.contrib import admin
from reversion.admin import VersionAdmin
from dashboard.models import *

class CategoryAdmin(VersionAdmin):
    list_display = ('title', 'priority')
admin.site.register(Category, CategoryAdmin)

class LinkAdmin(VersionAdmin):
    list_display = ('title', 'url')
admin.site.register(Link, LinkAdmin)

class CountdownAdmin(VersionAdmin):
    list_display = ('title', 'date', 'until')
admin.site.register(Countdown, CountdownAdmin)

def update_remote_image(modeladmin, request, queryset):
    for image in queryset:
        image.update()
update_remote_image.short_description = 'Update selected remote images'
        
class RemoteImageAdmin(VersionAdmin):
    list_display = ('title', 'source', 'last_update', 'active')
    actions = [update_remote_image]
admin.site.register(RemoteImage, RemoteImageAdmin)

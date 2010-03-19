from django.contrib import admin
from stream.models import Feed, Item

def check_feed(modeladmin, request, queryset):
    for feed in queryset:
        feed.check()
check_feed.short_description = 'Check feed for updates'

class FeedAdmin(admin.ModelAdmin):
    list_display = ('url',)
    actions = [check_feed]
    
admin.site.register(Feed, FeedAdmin)
admin.site.register(Item)

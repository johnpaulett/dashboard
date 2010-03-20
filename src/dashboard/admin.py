from django.contrib import admin
from reversion.admin import VersionAdmin
from dashboard.models import Category, Link

class CategoryAdmin(VersionAdmin):
    list_display = ('title', 'priority')
admin.site.register(Category, CategoryAdmin)

class LinkAdmin(VersionAdmin):
    list_display = ('title', 'url')
admin.site.register(Link, LinkAdmin)

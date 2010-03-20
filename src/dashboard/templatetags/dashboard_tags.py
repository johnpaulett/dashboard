from beehat.template import render
from dashboard.models import Category
from debug_toolbar.debug.version import DebugVersions
from django import template

register = template.Library()

@register.simple_tag
def versions_widget():
    versions = DebugVersions().get_versions()

    return render('dashboard/versions_widget.html',
                  {'versions': versions})

@register.simple_tag
def links_widget():
    categories = Category.objects.all()
    return render('dashboard/links_widget.html',
                  {'categories': categories})

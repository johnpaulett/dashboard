from beehat.template import render
from debug_toolbar.debug.version import DebugVersions
from django import template

register = template.Library()

@register.simple_tag
def versions_widget():
    versions = DebugVersions().get_versions()

    return render('dashboard/versions_widget.html',
                  {'versions': versions})


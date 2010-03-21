from beehat.template import render
from dashboard.models import Category, Countdown
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

@register.simple_tag
def countdowns_widget():
    countdowns = Countdown.objects.upcoming()
    return render('dashboard/countdowns_widget.html',
                  {'countdowns': countdowns,
                   'next_countdown': countdowns[0],
                   'later_countdowns': countdowns[1:]})
    

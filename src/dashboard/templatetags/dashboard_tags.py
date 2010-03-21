from dashboard.models import Category, Countdown, RemoteImage
from debug_toolbar.debug.version import DebugVersions
from django import template

register = template.Library()

@register.inclusion_tag('dashboard/versions_widget.html')
def versions_widget():
    return {'versions': DebugVersions().get_versions()}

@register.inclusion_tag('dashboard/links_widget.html')
def links_widget():
    return {'categories': Category.objects.all()}

@register.inclusion_tag('dashboard/countdowns_widget.html')
def countdowns_widget():
    countdowns = Countdown.objects.upcoming()
    return {'countdowns': countdowns,
            'next_countdown': countdowns[0],
            'later_countdowns': countdowns[1:]}
    
@register.inclusion_tag('dashboard/remote_images_widget.html',
                        takes_context=True)
def remote_images_widget(context):
    return {'images': RemoteImage.objects.filter(active=True),
            #TODO seems like the template should be able to get a RequestContext
            # but I am having issues doing so, so just pass the relevant
            # variable
            # http://squeeville.com/2009/01/27/django-templatetag-requestcontext-and-inclusion_tag/
            'MEDIA_URL': context['MEDIA_URL']}


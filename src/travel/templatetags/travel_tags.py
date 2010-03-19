from beehat.template import render
from django import template
from travel.models import ScheduledDeparture

register = template.Library()

@register.simple_tag
def upcoming_departures(number):

    return render('travel/upcoming_departures_widget.html',
                  {'departures': ScheduledDeparture.objects.upcoming()[0:number]})


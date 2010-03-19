from beehat.template import render
from django import template
from travel.models import ScheduledDeparture

register = template.Library()

def upcoming(direction, number):
    return ScheduledDeparture.objects.upcoming(direction)[0:number]

@register.simple_tag
def upcoming_departures(number):
    east = upcoming('E', number)
    west = upcoming('W', number)
    departures = [{'east': east[i], 'west': west[i]}
                  for i in xrange(0, number)]
    return render('travel/upcoming_departures_widget.html',
                  {'departures': departures})


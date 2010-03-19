from beehat.template import render
from django import template
from travel.models import ScheduledDeparture

register = template.Library()

def upcoming(direction, number):
    return ScheduledDeparture.objects.upcoming(direction)[0:number]

def add_row(index, east, west):
    row = {}
    if len(east) > index:
        row['east'] = east[index]
    if len(west) > index:
        row['west'] = west[index]
    return row
    
@register.simple_tag
def upcoming_departures(number):
    east = upcoming('E', number)
    west = upcoming('W', number)
    
    departures = [add_row(i, east, west)
                  for i in xrange(0, number)]
    return render('travel/upcoming_departures_widget.html',
                  {'departures': departures})


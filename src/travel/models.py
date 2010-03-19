from datetime import datetime
from django.db import models


class DepartureManager(models.Manager):
    def upcoming(self, direction):
        return self.filter(direction=direction,
                           time__gt=datetime.now().time())

DIRECTION_CHOICES = (
    ('E', 'Eastbound'),
    ('W', 'Westbound'),
    )

class ScheduledDeparture(models.Model):
    time = models.TimeField(db_index=True)
    direction = models.CharField(max_length=1,
                                 choices=DIRECTION_CHOICES,
                                 db_index=True)
    #location
    #day
    
    objects = DepartureManager()

    def __unicode__(self):
        return '%s %s' % (self.time.isoformat(), self.get_direction_display())

    class Meta:
        ordering = ['time']

from datetime import date, datetime, time, timedelta
from django.db import models


class DepartureManager(models.Manager):
    def upcoming(self, direction, now=None):
        # allow upcoming() to be tested by setting current time
        if now is None:
            now = datetime.now().time()

        # get the datetime.time object that is 24 hours in the future
        #future = (datetime.combine(date.today(), now) + timedelta(1)).time()
        #TODO rollover past midnight 
        return self.filter(direction=direction,
                           time__gt=now)
                           #time__range=(now, future))

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

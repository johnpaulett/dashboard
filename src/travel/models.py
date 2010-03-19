from datetime import datetime
from django.db import models


class DepartureManager(models.Manager):
    def upcoming(self):
        return self.filter(time__gt=datetime.now().time())

class ScheduledDeparture(models.Model):
    time = models.TimeField()

    objects = DepartureManager()

    def __unicode__(self):
        return self.time.isoformat()

    class Meta:
        ordering = ['time']

from datetime import time
from django.test import TestCase
from travel.models import *

def departures(times):
    return [ScheduledDeparture.objects.create(time=time, direction='W')
            for time in times]

class UpcomingTest(TestCase):
    def assertUpcomingCount(self, expected, now):
        self.assertEqual(expected,
                         ScheduledDeparture.objects.upcoming('W', now=now).count())
        
    def test_upcoming(self):
        departures([time(3, 0), time(4, 0), time(5, 0)])
        self.assertUpcomingCount(3, time(2, 0))

    def test_across_day(self):
        departures([time(1, 0), time(23, 0), time(2, 0)])
        self.assertUpcomingCount(1, time(22, 0)) #TODO arguably 3


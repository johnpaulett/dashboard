from datetime import date, timedelta
from django.test import TestCase
from dashboard.models import Countdown

def make_countdown(title, year=2010, month=3, day=21):
    return Countdown.objects.create(title=title,
                                    date=date(year, month, day))
    
class CountdownTest(TestCase):
    def test_upcoming(self):
        a = make_countdown('a', day=20)
        b = make_countdown('b', day=21)
        c = make_countdown('c', day=22)
        
        upcoming = Countdown.objects.upcoming(today=date(2010, 3, 21))
        self.assertEqual(2, upcoming.count())
        self.assertTrue(b in upcoming)
        self.assertTrue(c in upcoming)

    def test_until_future(self):
        c = make_countdown('c', day=23)
        self.assertEqual(timedelta(days=2), c.until(today=date(2010, 3, 21)))

    def test_until_past(self):
        c = make_countdown('c', day=20)
        self.assertEqual(timedelta(days=-1), c.until(today=date(2010, 3, 21)))

    def test_until_today(self):
        c = make_countdown('c', day=21)
        self.assertEqual(timedelta(days=0), c.until(today=date(2010, 3, 21)))

    def test_ordering(self):
        a = make_countdown('a', day=22)
        b = make_countdown('b', day=21)
        c = make_countdown('c', day=24)
        
        upcoming = Countdown.objects.upcoming(today=date(2010, 3, 1))

        self.assertEqual(b, upcoming[0])
        self.assertEqual(a, upcoming[1])
        self.assertEqual(c, upcoming[2])
        

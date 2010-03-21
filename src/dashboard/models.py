from datetime import date
from django.db import models

def default(value, default):
    return value if value is not None else default

class Link(models.Model):
    title = models.TextField(blank=True)
    url = models.URLField(verify_exists=False)
    category = models.ForeignKey('Category')
    
    def __unicode__(self):
        return self.title if self.title else self.url

class Category(models.Model):
    title = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=10)
    
    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['priority']


class CountdownManager(models.Manager):
    def upcoming(self, today=None):
        # allow upcoming() to be tested by setting current date
        today = default(today, date.today())

        return self.filter(date__gte=today)

class Countdown(models.Model):
    title = models.TextField()
    date = models.DateField()

    objects = CountdownManager()

    def until(self, today=None):
        today = default(today, date.today())
        return self.date - today
    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['date']

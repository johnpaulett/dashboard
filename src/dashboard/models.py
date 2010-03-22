from datetime import date, datetime
from django.core.files.base import ContentFile
from django.db import models
from httplib2 import Http
from urlparse import urlparse

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


class RemoteImage(models.Model):
    source = models.URLField(verify_exists=False)
    title = models.TextField(blank=True)
    link = models.URLField(verify_exists=False, blank=True)
    image = models.ImageField(upload_to='uploads/remote_images', blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def _filename(self, now):
        return '%s%s' % (now, urlparse(self.source).path.replace('/', '_'))
    
    def update(self):
        if not self.active:
            return
        
        h = Http('.httplib2-cache')
        # TODO be smart with caching and handle Not Modified
        resp, content = h.request(self.source)
        #import pdb; pdb.set_trace()
        if resp.status in [200, 304]:
            now = datetime.now()
            if resp.status == 200:
                self.image.save(self._filename(now), ContentFile(content))
            self.last_update = now
            self.save()

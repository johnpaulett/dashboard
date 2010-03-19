from datetime import datetime
from django.db import models
import feedparser

class Item(models.Model):
    guid = models.TextField(null=True, blank=True, db_index=True)
    value = models.TextField(null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    feed = models.ForeignKey('Feed')

    def __unicode__(self):
        return unicode(self.value)

    class Meta:
        ordering = ['time']

class Feed(models.Model):
    title = models.TextField(null=True, blank=True)
    url = models.URLField()

    def check(self):
        feed = feedparser.parse(self.url)
        for entry in feed.entries:
            guid = entry.guid
            existing = Item.objects.filter(feed=self, guid=guid)
            if len(existing) == 0:
                Item.objects.create(guid=guid,
                                    url=entry.link,
                                    time=datetime(*entry.date_parsed[0:6]),
                                    value=entry.title,
                                    feed=self)
    def __unicode__(self):
        return unicode(self.url)

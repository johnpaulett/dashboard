from django.db import models

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

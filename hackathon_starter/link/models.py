from django.db import models

# Create your models here.
class Link(models.Model):
    name = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=1000)

    class Meta:
        ordering = ('-time_created',)


class BoxObj(models.Model):
    name = models.CharField(max_length=255)
    is_link = models.BooleanField(default=True)
    time_created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    parrent_boxes = models.ForeignKey('link.BoxObj', null=True, blank=True)

    class Meta:
        ordering = ('-time_created',)

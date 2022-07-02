from datetime import datetime
import os
from uuid import uuid4
from django.conf import settings
from django.db import models
import pytz

from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize

from givito.account.models import User, randStr

def upload_placeholder(instance, filename):
    full_path = os.path.join(settings.MEDIA_ROOT, 'project', str(instance.uuid), 'placeholder')
    if(os.path.exists(full_path)):
        for file in os.listdir(full_path):
            if("placeholder" in file):
                os.remove(full_path + "/" + file)
    file = os.path.join('project', str(instance.uuid), 'placeholder', f'placeholder-{randStr()}.png')
    return file

CHOICES = [
        ('UNASSIGNED', 'Unassigned'),
        ('ASSIGNED', 'Assigned'),
        ('IN_PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
        ('CANCELED', 'Canceled')]

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(primary_key=True)
    description = models.TextField()
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now(tz=pytz.UTC)
        super(User, self).delete(*args, **kwargs)

class Project(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, default=uuid4)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='owner')
    registrant = models.CharField(max_length=36, null=True, blank=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    expected_duration = models.DurationField(null=True, blank=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=11, choices=CHOICES, default='UNASSIGNED')
    deleted_at = models.DateTimeField(null=True, blank=True)
    placeholder = ProcessedImageField(verbose_name='File foto',
        upload_to=upload_placeholder,
        format='PNG',
        processors=[SmartResize(1280, 720)],
        options={'quality': 85}, blank=True, null=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now(tz=pytz.UTC)
        super(User, self).delete(*args, **kwargs)

class ProjectRegistrant(models.Model):
    uuid = models.CharField(max_length=36, primary_key=True, default=uuid4)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='registrants')
    offering_price = models.BigIntegerField()
    description = models.TextField(null=True, blank=True)
    offering_duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='registrants')

    def status(self) :
        if(self.project.registrant == None):
            return "UNASSIGNED"
        elif(self.project.registrant == self.uuid):
            return self.project.status
        else:
            return "DENIED"

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now(tz=pytz.UTC)
        super(User, self).delete(*args, **kwargs)

    def __str__(self):
        return self.owner.name
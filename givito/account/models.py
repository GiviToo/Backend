from datetime import datetime
import os
import random
import string
from uuid import uuid4
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize
import pytz

from givito.account.managers import UserManager

def randStr(chars = string.ascii_lowercase + string.ascii_uppercase + string.digits, N=64):
	return ''.join(random.choice(chars) for _ in range(N))

def upload_avatar(instance, filename):
    full_path = os.path.join(settings.MEDIA_ROOT, 'users', str(instance.uuid), 'avatar')
    if(os.path.exists(full_path)):
        for file in os.listdir(full_path):
            if("avatar" in file):
                os.remove(full_path + "/" + file)
    file = os.path.join('users', str(instance.uuid), 'avatar', f'avatar-{randStr()}.png')
    return file
    
class User(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(null=False, blank=False, default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    uuid = models.CharField(max_length=36, default=uuid4, unique=True)
    name = models.CharField(max_length=36)
    phone = models.CharField(max_length=15, null=True, blank=True, default="")
    email = models.EmailField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    avatar = ProcessedImageField(verbose_name='File foto',
        upload_to=upload_avatar,
        format='PNG',
        processors=[SmartResize(600, 800)],
        options={'quality': 85}, blank=True, null=True)

    USERNAME_FIELD = 'email'
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    def delete(self, *args, **kwargs):
        self.deleted_at = datetime.now(tz=pytz.UTC)
        super(User, self).delete(*args, **kwargs)

    def __str__(self):
        return self.email
    
        
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(_('Full name'), max_length = 200, blank=False, null=False)
    email = models.EmailField(_('email address'), unique=True, blank=False, null=False)
    
# coding=utf8
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from managers import UserManager, AdministratorManager


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    username = models.CharField(_('username'), max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.email


class Administrator(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    username = models.CharField(_('username'), max_length=30, unique=True)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    is_staff = True

    objects = AdministratorManager()

    class Meta:
        verbose_name = _('administrator')
        verbose_name_plural = _('administrators')

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def get_group_permissions(self, obj=None):
        return set()

    def get_all_permissions(self, obj=None):
        return set()

    def has_perm(self, perm, obj=None):
        return True

    def has_perms(self, perm_list, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

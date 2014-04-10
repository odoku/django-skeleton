# coding=utf8
from __future__ import unicode_literals

from django.contrib import admin

from models import User, Administrator


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class AdministratorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Administrator, AdministratorAdmin)

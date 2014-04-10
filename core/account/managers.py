# coding=utf8
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(
            email=email,
            last_login=timezone.now(),
            **extra_fields
        )
        user.set_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        return self._create_user(email, **extra_fields)


class AdministratorManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=username,
            last_login=timezone.now(),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username, password, **extra_fields)

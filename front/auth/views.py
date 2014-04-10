# coding=utf8
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import resolve_url
from django.utils.http import is_safe_url
from django.views.generic import FormView, RedirectView


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'auth/login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        try:
            url = super(LoginView, self).get_success_url()
        except ImproperlyConfigured:
            url = ''
        url = self.request.REQUEST.get(REDIRECT_FIELD_NAME, url)
        if not is_safe_url(url=url, host=self.request.get_host()):
            url = resolve_url(settings.LOGIN_REDIRECT_URL)
        return url

login = LoginView.as_view()


class LogoutView(RedirectView):
    permanent = False

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        url = super(LogoutView, self).get_redirect_url(*args, **kwargs) or ''
        url = self.request.REQUEST.get(REDIRECT_FIELD_NAME, url)
        if not is_safe_url(url=url, host=self.request.get_host()):
            url = '/'
        return url

logout = LogoutView.as_view()

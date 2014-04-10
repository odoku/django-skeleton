# coding=utf8
from __future__ import unicode_literals

from django import forms

from core.account.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        model = super(RegistrationForm, self).save(commit=False)

        model.set_password(self.cleaned_data['password'])

        if (commit):
            model.save()
        return model

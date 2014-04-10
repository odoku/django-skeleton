# coding=utf8
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = 'home/index.html'

index = login_required(IndexView.as_view())

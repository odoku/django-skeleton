# coding=utf8
from __future__ import unicode_literals

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'

index = IndexView.as_view()

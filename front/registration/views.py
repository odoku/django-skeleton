# coding=utf8
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from forms import RegistrationForm


class IndexView(FormView):
    template_name = 'registration/index.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('registration:thanks')

    def form_valid(self, form):
        form.save()
        return super(IndexView, self).form_valid(form)

index = IndexView.as_view()


class ThanksView(TemplateView):
    template_name = 'registration/thanks.html'

thanks = ThanksView.as_view()

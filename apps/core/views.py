# -*- coding: utf-8 -*-

from django.views.generic.base import (
    TemplateView
)


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self):
        data = super(Home, self).get_context_data()
        return data


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.views.generic import FormView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = 'home.html'

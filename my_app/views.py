# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = 'index.html'
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'host', views.hostEvent, name='host'),
    url(r'register', views.registerUser, name='register')
]
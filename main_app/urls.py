# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    # Circle endpoints
    url(r'circle/host', views.hostCircle),
    url(r'circle/delete', views.deleteCircle),
    url(r'circle/move', views.moveCircle),
    url(r'circle/repeat', views.repeatCircle),
    url(r'circle/participate', views.participateCircle),
    url(r'circle/exit', views.exitCircle),

    # user endpoints
    url(r'user/register', views.registerUser),
    url(r'user/delete', views.deleteUser),
]
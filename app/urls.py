#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - urls.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

from django.conf.urls import url

from . import views

urlpatterns = [
    # A view named "home" is referenced in a few places.
    # Make sure to update the references if you change or delete this url line!
    url(r"^$", views.home, name="home"),
]

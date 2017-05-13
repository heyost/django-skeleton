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
    url(r"^provider/(?P<provider>[a-z]+)/login$", views.login,
        name="oauth_login"),
    url(r"^provider/(?P<provider>[a-z]+)/complete$", views.complete,
        name="oauth_complete"),
    url(r"^associate$", views.associate, name="oauth_associate"),

]
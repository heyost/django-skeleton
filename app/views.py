#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - views.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

import django.views.generic


class Home(django.views.generic.TemplateView):
    def __init__(self):
        super(Home, self).__init__()

    template_name = "home.html"
home = Home.as_view()

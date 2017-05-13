#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - context_processors.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

from django.conf import settings


def google_analytics(request):
    """
    Add Google Analytics tracking context
    """
    return {'GA': settings.GOOGLE_ANALYTICS_KEY}

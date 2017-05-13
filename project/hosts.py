#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - hosts.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 4:48 PM
#
#

from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
                         host(r'www', settings.ROOT_URLCONF, name='www'),
                         host(r'(\w+)', 'path.to.custom_urls', name='wildcard'),
                         )

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - admin.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

from django.contrib import admin

from . import models


@admin.register(models.OAuthUser)
class OAuthUserAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'provider', 'uid', 'email', 'user']

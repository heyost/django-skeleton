#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - authbackend.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

import django.contrib.auth.backends

from .models import OAuthUser


class OAuthBackend(django.contrib.auth.backends.ModelBackend):
    """
    A Django authorization backend that is used to log in a user from an
    OAuthUser object

    """

    def __init__(self):
        pass

    def authenticate(self, oauthuser, **kwargs):
        if not isinstance(oauthuser, OAuthUser):
            return

        if oauthuser.user is not None:
            return oauthuser.user


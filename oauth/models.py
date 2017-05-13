#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mdfjr - models.py
#
#  Created by PyCharm.
#  User: fajar
#  Date: 5/13/17
#  Time: 3:50 PM
#
#

from django.db import models


class OAuthUser(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    user = models.ForeignKey("auth.User", null=True, blank=True,
                             on_delete=models.SET_NULL,
                             )
    email = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = "OAuth User"
        verbose_name_plural = "OAuth Users"
        unique_together = ['provider', 'uid']

    def __str__(self):
        return self.email or "{} of {}".format(self.uid, self.provider)

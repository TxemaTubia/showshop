# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shoe

admin.site.register(Shoe)

from .models import Purchase

admin.site.register(Purchase)

# Register your models here.

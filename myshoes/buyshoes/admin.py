# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Shoe

admin.site.register(Shoe)

from .models import purchase

admin.site.register(purchase)

# Register your models here.

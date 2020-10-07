# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime
import time

# Create your models here.
class Shoe(models.Model):
	shoe_name = models.CharField(max_length=50)
	shoe_description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	shoe_price = models.DecimalField(max_digits=6, decimal_places=4, default=0)
	def __str__(self):
		return self.shoe_name
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Purchase(models.Model):
    purchase = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    active = models.IntegerField(default=0)
    modify = models.IntegerField(default=0)
    notified = models.IntegerField(default=0)
    buy_date = models.DateTimeField(auto_now=True)
    def was_buyed_recently(self):
        return self.buy_date >= timezone.now() - datetime.timedelta(days=1)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Shoe



#def index(request):
#	latest_shoe_list = Shoe.objects.order_by('-pub_date')[:5]
#	output = ', '.join([q.shoe_name for q in latest_shoe_list])
#	return HttpResponse(output)
#   #return HttpResponse("You're at the Bernini ShoesShop index.")

def index(request):
    latest_shoe_list = Shoe.objects.order_by('-pub_date')[:5]
    template = loader.get_template('buyshoes/index.html')
    context = {
        'latest_shoe_list': latest_shoe_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, shoe_id):
    return HttpResponse("You're looking the shoe %s." % shoe_id)

def purchase(request, purchase_id):
    response = "This is a purchase %s."
    return HttpResponse(response % purchase_id)

def description(request, shoe_id):
	my_shoe = Shoe.objects.get(id=shoe_id)
	output = "Shoe %s description: %s" % (shoe_id, my_shoe.shoe_description)
	return HttpResponse(output)

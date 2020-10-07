# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import get_object_or_404, render

from django.template import loader

from .models import Shoe, Purchase

from django.views.decorators.csrf import csrf_exempt

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

#ref myshoes/buyshoes/templates/buyshoes/detail.html
@csrf_exempt
def detail(request, shoe_id):
    #return HttpResponse("You're looking the shoe %s." % shoe_id)
    try:
        shoe = Shoe.objects.get(pk=shoe_id)
    except Shoe.DoesNotExist:
        raise Http404("Shoe does not exist")
    return render(request, 'buyshoes/detail.html', {'shoe': shoe})

@csrf_exempt
def shoe_detail(request, shoe_id):
    try:
    	shoe = Shoe.objects.get(pk=shoe_id)
    except Shoe.DoesNotExist:
        raise Http404("Shoe does not exist")
    if request.method == 'GET':
        serializer = DeviceSerializeer(shoe)
        return JsonResponse(serializer.shoe_name)

def purchase(request, purchase_id):
    #response = "This is a purchase %s."
    #return HttpResponse(response % purchase_id)
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    return render(request, 'buyshoes/purchase.html', {'purchase': purchase})

def description(request, shoe_id):
	my_shoe = Shoe.objects.get(id=shoe_id)
	output = "Shoe %s description: %s" % (shoe_id, my_shoe.shoe_description)
	return HttpResponse(output)

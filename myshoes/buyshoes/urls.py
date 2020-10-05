from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #http://127.0.0.1:8080/buyshoes/1/
    url(r'^(?P<shoe_id>[0-9]+)/$', views.detail, name='detail'),
    #http://127.0.0.1:8080/buyshoes/1/purchase/
    url(r'^(?P<purchase_id>[0-9]+)/purchase/$', views.purchase, name='purchase'),
    url(r'^(?P<shoe_id>[0-9]+)/description/$', views.description, name='description'),
]
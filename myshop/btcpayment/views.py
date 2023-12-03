from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings

import datetime
import json
import requests
import uuid
import os

from .models import *
from orders.models import Order


# Create your views here.

def home(request):

    products = Product.objects.all()
    return render(request, 'product.html', context = {"products":products})

def exchanged_rate(amount):
    url = "https://www.blockonomics.co/api/price?currency=USD"
    r = requests.get(url)
    response = r.json()
    return float(amount)/response['price']

def track_invoice(request, pk):
    invoice_id = pk
    invoice = Invoice.objects.get(id=invoice_id)
    #Obtener Orden
    order_id_orders = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id_orders)
    #Hacer la suma de Items de compra
    total = 0
    for item in order.items.all():
        total += item.get_cost()
    data = {
            'order_id':invoice.order_id,
            'bits':invoice.btcvalue/1e8,
            'value':total,
            'addr': invoice.address,
            'status':Invoice.STATUS_CHOICES[invoice.status+1][1],
            'invoice_status': invoice.status,
            'order': invoice.invoce_order,
        }
    if (invoice.received):
        data['paid'] =  invoice.received/1e8
        if (int(invoice.btcvalue) <= int(invoice.received)):
            data['path'] = invoice.product.product_image.url
    else:
        data['paid'] = 0  

    return render(request,'invoice.html',context=data)

def create_payment(request):
    #Obtener Orden
    order_id_orders = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id_orders)
    #Hacer la suma de Items de compra
    total = 0
    for item in order.items.all():
        total += item.get_cost()
               
    ###############################################
    # product_id = pk
    # product = Product.objects.get(id=product_id)
    ###############################################
    #Solicitar dirrecion de pago
    url = 'https://www.blockonomics.co/api/new_address?match_account=6rdMge'
    headers = {'Authorization': "Bearer " + settings.API_KEY}
    print("api key ",settings.API_KEY)
    r = requests.post(url, headers=headers)
    print(r.json())

    if r.status_code == 200:
        address = r.json()['address']
        #change
        bits = exchanged_rate(total)
        order_id = uuid.uuid1()
        invoice = Invoice.objects.create(order_id=order_id,
                                address=address,btcvalue=bits*1e8, invoce_order=order)
        return HttpResponseRedirect(reverse('payments_btc:track_payment', kwargs={'pk':invoice.id}))
    else:
        print(r.status_code, r.text)
        return HttpResponse("Some Error, Try Again!")
    
def receive_payment(request):
    
    if (request.method != 'GET'):
        return 
    
    txid  = request.GET.get('txid')
    value = request.GET.get('value')
    status = request.GET.get('status')
    addr = request.GET.get('addr')

    invoice = Invoice.objects.get(address = addr)
    
    invoice.status = int(status)
    if (int(status) == 2):
        invoice.received = value
    invoice.txid = txid
    invoice.save()
    return HttpResponse(200)

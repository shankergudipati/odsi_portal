from django.shortcuts import render
from urllib import urlencode
from django.http import *
from django.conf import settings
import pdb

import urllib2
import simplejson as json
import time
import json
import ast

def odsi_portal_homepage(request):
    return render(request,'homepage.html')
 
def loginbutton_openstack(request):
   # pdb.set_trace()
    openstack_username=request.POST.get('openstack_username')
    openstack_password=request.POST.get('openstack_password')
    service_id=request.POST.get('os_form_serviceid')
    product_id=request.POST.get('os_form_productid')
    productname=request.POST.get('os_form_productname')
    os=request.POST.get('os_form_os')
    version=request.POST.get('os_form_version')
    architecture=request.POST.get('os_form_architecture')    
    dic={"openstack_username":openstack_username,"openstack_password":openstack_password}
    url="http://10.233.52.111:8001/authenticate/"
    jsondata = json.dumps(dic)
    req = urllib2.Request(url, \
                         headers = {

                                     "Content-Type": "application/json",
                                   },                        \
                         data = jsondata)
    f = urllib2.urlopen(req)
    response = f.read()
    res = json.loads(response)

    return render(request,"totaldetails.html",locals())

def final_form_submit(request):
    pdb.set_trace()
    service_id=request.POST.get('final_form_serviceid')
    product_id=request.POST.get('final_form_productid')
    productname=request.POST.get('final_form_productname')
    version=request.POST.get('final_form_version')
    architecture=request.POST.get('final_form_architecture')
    type="cloud" 
       
    return render(request,"page.html")


from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .services import list_certificates
# Create your views here.

    
@api_view(['GET'])    
def certificates(request):
    certs, errors = list_certificates()
    
    cert_map = []
    for cert in certs:
        print(type(cert.live_dir))
        cert_map.append({
            'cert': cert.cert,  
            'privkey': cert.privkey,
            'fullchain': cert.chain,
            'live_dir': cert.live_dir
        })
    
    print(cert_map)
    return Response(cert_map)
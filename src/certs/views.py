from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import permissions, serializers, status, viewsets
from .services import list_certificates
from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectView(viewsets.ModelViewSet):
    """
    """
    
    serializer_class = ProjectSerializer
    
    queryset = Project.objects.all()
    
    permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly, 
    )
    
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
    
    return Response(cert_map)
from django.urls import path, re_path, include
from rest_framework import routers
from .views         import ProjectView


router = routers.SimpleRouter()
router.register(r'projects', ProjectView)

urlpatterns = [
    re_path('^api/v1/', include(router.urls))
]
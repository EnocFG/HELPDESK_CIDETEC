from HelpdeskApp.models import *
from HelpdeskApp.views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('Estatus', EstatusViewSet)
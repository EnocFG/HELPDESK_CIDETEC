from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'area', views.areaViewSet)
# router.register(r'proyecto', views.proyectoViewSet)
# router.register(r'rol', views.rolViewSet)
# router.register(r'especialidad', views.espViewSet)
# router.register(r'prioridad', views.prioViewSet)
# router.register(r'usuario', views.usuarioViewSet)
# router.register(r'especialista', views.especViewSet)
# router.register(r'ticket', views.ticketViewSet)
# router.register(r'estatus', views.EstatusViewSet)
# router.register(r'estatus_ticket', views.EstatusTicketViewSet)
# router.register(r'comentario', views.ComentarioViewSet)
# router.register(r'historial_ticket', views.HistorialViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ticket/', views.TicketApi),
    path('ticket/([0-9])', views.TicketApi)


]

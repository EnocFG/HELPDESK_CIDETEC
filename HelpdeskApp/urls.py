from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register("ejemplo", views.ejemploview, basename="mi_ejemplo")

router.register("rol", views.RolView, basename="Rol")
router.register("prioridad", views.PrioridadView, basename="Prioridad")
router.register("estatus_ticket", views.EstatusTicketView, basename="Estatus-Ticket")
urlpatterns = [
    # Rutas de viewsets
    path("", include(router.urls)),
    # Rutas de vistas basadas en clases
    path("ticket/", login_required(views.TicketView.as_view())),
    path("ticket/<int:id>/", login_required(views.TicketDetalle.as_view())),
    path("proyecto/", login_required(views.ProyectoView.as_view())),
    path("proyecto/<int:id>/", login_required(views.ProyectoDetalle.as_view())),
    path("area/", login_required(views.AreaView.as_view())),
    path("area/<int:id>/", login_required(views.AreaDetalle.as_view())),
    path("usuario/", login_required(views.UsuarioView.as_view())),
    path("usuario/<int:id>/", login_required(views.UsuarioDetalle.as_view())),
    path("comentario", login_required(views.ComentarioView.as_view())),
    path("comentario/<int:id>/", login_required(views.ComentarioDetalle.as_view())),
    path("especialista/", login_required(views.Especialista.as_view())),
    path("especialista/<int:id>/", login_required(views.EspecialistaDetalle.as_view())),
    path("estatus/", views.EstatusView.as_view()),
    path("estatus/<int:id>/", views.EstatusDetalle.as_view()),
]

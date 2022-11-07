from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('ticket/', login_required(views.TicketView.as_view())),
    path('ticket/<int:id>/', login_required(views.TicketDetalle.as_view())),

    path('proyecto/', login_required(views.ProyectoView.as_view())),
    path('proyecto/<int:id>/', login_required(views.ProyectoDetalle.as_view())),

    path('area/', login_required(views.AreaView.as_view())),
    path('area/<int:id>/', login_required(views.AreaDetalle.as_view())),

    path('usuario/', login_required(views.UsuarioView.as_view()), name='usuario'),
    path('usuario/<int:id>/', login_required(views.UsuarioDetalle.as_view()), name='usuario_detalle'),

    path('comentario', login_required(views.ComentarioView.as_view()), name='comentario'),
    path('comentario/<int:id>/', login_required(views.ComentarioDetalle.as_view()), name='comentario_detalle'),

    path('especialista', login_required(views.EspecialistaView.as_view())),
    path('especialista/<int:id>/', login_required(views.EspecDetalle.as_view())),


]

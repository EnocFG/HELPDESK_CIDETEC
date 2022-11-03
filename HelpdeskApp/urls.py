from django.urls import include, path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('ticket/', views.TicketView.as_view()),
    path('ticket/<int:id>/', views.TicketDetalle.as_view()),

    path('proyecto/', login_required(views.ProyectoView.as_view())),
    path('proyecto/<int:id>/', views.ProyectoDetalle.as_view()),

    path('area/', views.AreaView.as_view()),
    path('area/<int:id>/', views.AreaDetalle.as_view()),

    path('usuario/', views.UsuarioView.as_view(), name='usuario'),
    path('usuario/<int:id>/', views.UsuarioDetalle.as_view(), name='usuario_detalle'),

    path('comentario', views.ComentarioView.as_view(), name='comentario'),
    path('comentario/<int:id>/', views.ComentarioDetalle.as_view(), name='comentario_detalle'),

    path('especialista', views.EspecialistaView.as_view()),
    path('especialista/<int:id>/', views.EspecDetalle.as_view()),
]

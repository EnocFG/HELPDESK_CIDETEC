from django.urls import include, path
from . import views

urlpatterns = [

    path('ticket/', views.TicketView.as_view()),
    path('ticket/<int:id>/', views.TicketDetalle.as_view()),

    path('proyecto/', views.ProyectoView.as_view()),
    path('proyecto/<int:id>/', views.ProyectoDetalle.as_view()),

    path('area/', views.AreaView.as_view()),
    path('area/<int:id>/', views.AreaDetalle.as_view()),

    path('usuario/', views.UsuarioView.as_view(), name='usuario'),
    path('usuario/<int:id>/', views.UsuarioDetalle.as_view(), name='usuario_detalle'),

]

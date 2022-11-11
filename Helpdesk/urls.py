from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from rest_framework.schemas import get_schema_view
from Profiles.views import *

urlpatterns = [
    # OAUTH urls
    path("o/", include("oauth2_provider.urls", namespace="oauth_provider")),
    path("", BienvenidaView.as_view(), name="bienvenida"),
    path("", include("HelpdeskApp.urls")),
    # Rutas para creación y logeo de cuentas
    path("registro/", SignUpView.as_view(), name="sign_up"),
    path("login/", SignInView.as_view(), name="sign_in"),
    path("logout/", SignOutView.as_view(), name="sign_out"),
    path("cuenta/", include("allauth.urls"), name="cuenta"),
    # Rutas para generar documentación de la Api
    path(
        "openapi/",
        get_schema_view(
            title="Servicio REST",
            description="Documentación del servicio REST para el sistema Helpdesk del CIDETEC",
        ),
        name="openapi-schema",
    ),
    path(
        "docs/",
        TemplateView.as_view(
            template_name="documentation.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    # Ruta del sitio administrador de Django
    path("admin/", admin.site.urls),
]

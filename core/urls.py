from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path(
        "",
        views.home,
        name="home",
    ),
    path(
        "dashboard/empresa/<int:company_id>/",
        views.company_dashboard,
        name="company_dashboard",
    ),
    path(
        "dashboard/empresa/<int:company_id>/campanas/nueva/",
        views.campaign_create,
        name="campaign_create",
    ),
    path(
        "dashboard/campana/<int:campaign_id>/",
        views.campaign_detail,
        name="campaign_detail",
    ),
    path(
        "dashboard/campana/<int:campaign_id>/difusiones/importar/",
        views.diffusion_import,
        name="diffusion_import",
    ),
]

from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("",views.home,name="home"),
    # Companies
    path("companies/", views.company_list, name="companies"),
    path("companies/<int:company_id>/",views.company_dashboard,name="company_dashboard"),
    path("companies/create/",views.company_create,name="company_create"),

    # Campaigns
    path("companies/<int:company_id>/campaigns/nueva/",views.campaign_create,name="campaign_create"),
    path("campaigns/<int:campaign_id>/",views.campaign_detail,name="campaign_detail"),

    # Diffusions
    path("campaigns/<int:campaign_id>/difusiones/importar/",views.diffusion_import,name="diffusion_import"),
]

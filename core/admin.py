from django.contrib import admin

from unfold.admin import ModelAdmin

from .models import (
    Campaign,
    Company,
    Diffusion,
    DiffusionDailyMetric,
)


@admin.register(Company)
class CompanyAdmin(ModelAdmin):

    list_display = (
        "name",
        "code",
        "nit",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "name",
        "code",
        "nit",
    )


@admin.register(Campaign)
class CampaignAdmin(ModelAdmin):

    list_display = (
        "name",
        "company",
        "start_date",
        "end_date",
        "is_active",
        "created_at",
    )

    list_filter = (
        "company",
        "is_active",
    )

    search_fields = (
        "name",
        "company__name",
    )


@admin.register(Diffusion)
class DiffusionAdmin(ModelAdmin):

    list_display = (
        "name",
        "campaign",
        "classification",
        "diffusion_date",
        "total_sent",
        "total_delivered",
        "total_read",
        "total_responded",
        "total_failed",
    )

    list_filter = (
        "classification",
        "diffusion_date",
        "campaign__company",
    )

    search_fields = (
        "name",
        "campaign__name",
        "campaign__company__name",
    )


@admin.register(DiffusionDailyMetric)
class DiffusionDailyMetricAdmin(ModelAdmin):

    list_display = (
        "diffusion",
        "date",
        "sent",
        "delivered",
        "read",
        "failed",
    )

    list_filter = (
        "date",
    )

    search_fields = (
        "diffusion__name",
    )
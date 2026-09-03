

from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CampaignForm, DiffusionImportForm
from .models import Campaign, Company, Diffusion


# Create your views here.
def home(request):
    companies = Company.objects.filter(is_active=True)

    return render(
        request,
        "home.html",
        {
            "companies": companies,
        },
    )


def dashboard(request):
    companies = Company.objects.filter(is_active=True)

    return render(
        request,
        "dashboard/general.html",
        {
            "companies": companies,
        },
    )


def company_dashboard(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id,
        is_active=True,
    )

    campaigns = company.campaigns.all()

    diffusions = Diffusion.objects.filter(campaign__company=company)

    total_campaigns = campaigns.count()

    total_diffusions = diffusions.count()

    total_sent = diffusions.aggregate(total=Sum("total_sent"))["total"] or 0

    total_delivered = diffusions.aggregate(total=Sum("total_delivered"))["total"] or 0

    total_read = diffusions.aggregate(total=Sum("total_read"))["total"] or 0

    total_failed = diffusions.aggregate(total=Sum("total_failed"))["total"] or 0

    delivery_rate = (
        round(
            (total_delivered / total_sent) * 100,
            2,
        )
        if total_sent
        else 0
    )

    marketing = diffusions.filter(
        classification=Diffusion.Classification.MARKETING
    ).count()

    utility = diffusions.filter(classification=Diffusion.Classification.UTILITY).count()

    authentication = diffusions.filter(
        classification=Diffusion.Classification.AUTHENTICATION
    ).count()

    return render(
        request,
        "dashboard/company.html",
        {
            "company": company,
            "campaigns": campaigns,
            "total_campaigns": total_campaigns,
            "total_diffusions": total_diffusions,
            "total_sent": total_sent,
            "total_delivered": total_delivered,
            "total_read": total_read,
            "total_failed": total_failed,
            "delivery_rate": delivery_rate,
            "marketing": marketing,
            "utility": utility,
            "authentication": authentication,
        },
    )


def campaign_create(request, company_id):

    company = get_object_or_404(
        Company,
        id=company_id,
        is_active=True,
    )

    if request.method == "POST":

        form = CampaignForm(request.POST)

        if form.is_valid():

            campaign = form.save(commit=False)

            campaign.company = company

            campaign.save()

            return redirect(
                "company_dashboard",
                company_id=company.id,
            )

    else:

        form = CampaignForm()

    return render(
        request,
        "dashboard/campaign_form.html",
        {
            "company": company,
            "form": form,
        },
    )



def campaign_detail(request, campaign_id):

    campaign = get_object_or_404(
        Campaign.objects.select_related("company"),
        id=campaign_id,
        company__is_active=True,
    )

    diffusions = campaign.diffusions.all()

    total_sent = diffusions.aggregate(total=Sum("total_sent"))["total"] or 0

    total_delivered = diffusions.aggregate(total=Sum("total_delivered"))["total"] or 0

    total_read = diffusions.aggregate(total=Sum("total_read"))["total"] or 0

    total_responded = diffusions.aggregate(total=Sum("total_responded"))["total"] or 0

    total_failed = diffusions.aggregate(total=Sum("total_failed"))["total"] or 0

    delivery_rate = (
        round(
            (total_delivered / total_sent) * 100,
            2,
        )
        if total_sent
        else 0
    )

    return render(
        request,
        "dashboard/campaign_detail.html",
        {
            "campaign": campaign,
            "company": campaign.company,
            "diffusions": diffusions,
            "total_diffusions": diffusions.count(),
            "total_sent": total_sent,
            "total_delivered": total_delivered,
            "total_read": total_read,
            "total_responded": total_responded,
            "total_failed": total_failed,
            "delivery_rate": delivery_rate,
        },
    )


def diffusion_import(request, campaign_id):

    campaign = get_object_or_404(
        Campaign.objects.select_related(
            "company"
        ),
        id=campaign_id,
        company__is_active=True,
    )

    if request.method == "POST":

        form = DiffusionImportForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():

            uploaded_file = form.cleaned_data[
                "file"
            ]

            # Aquí posteriormente procesaremos
            # el CSV/XLSX de Conectly.

            return redirect(
                "campaign_detail",
                campaign_id=campaign.id,
            )

    else:

        form = DiffusionImportForm()

    return render(
        request,
        "dashboard/diffusion_import.html",
        {
            "campaign": campaign,
            "company": campaign.company,
            "form": form,
        },
    )
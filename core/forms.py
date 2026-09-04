from django import forms

from .models import Campaign, Company

class CompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = [
            "name",
            "code",
            "nit",
            "logo",
            "is_active",
        ]

        labels = {
            "name": "Nombre de la empresa",
            "code": "Código",
            "nit": "NIT",
            "logo": "Logo",
            "is_active": "Empresa activa",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Ej. Mi Empresa S.A.",
                }
            ),

            "code": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Ej. MI-EMPRESA",
                }
            ),

            "nit": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Ej. 123456789",
                }
            ),

            "logo": forms.ClearableFileInput(
                attrs={
                    "class": "file-input file-input-bordered w-full",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "checkbox checkbox-primary",
                }
            ),
        }


class CampaignForm(forms.ModelForm):

    class Meta:
        model = Campaign

        fields = [
            "name",
            "description",
            "start_date",
            "end_date",
            "is_active",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Ej. Campaña Primavera",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                    "placeholder": "Descripción de la campaña",
                    "rows": 4,
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "type": "date",
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "type": "date",
                }
            ),

            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "checkbox checkbox-primary",
                }
            ),
        }


class DiffusionImportForm(forms.Form):

    file = forms.FileField(
        label="Reporte de Conectly",
        help_text="Seleccione el archivo CSV o Excel exportado desde Conectly.",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "file-input file-input-bordered w-full",
                "accept": ".csv,.xlsx,.xls",
            }
        ),
    )
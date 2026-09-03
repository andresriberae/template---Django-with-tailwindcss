from django import forms

from .models import Campaign


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
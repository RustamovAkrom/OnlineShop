from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = {
            "first_name": forms.CharField(),
            "last_name": forms.CharField(),
            "email": forms.EmailField(),
            "address": forms.CharField(),
            "postal_code": USZipCodeField(),
            "city": forms.CharField(),
        }
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "firstName",
                    "placeholder": "",
                    "required": "",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "lastName",
                    "placeholder": "",
                    "required": "",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "you@example.comt",
                    "required": "",
                }
            ),
            "address": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "address",
                    "placeholder": "1234 Main st",
                    "required": "",
                }
            ),
            "postal_code": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "postal_code",
                    "placeholder": "format XXXXX or XXXXX-XXXX",
                    "required": "",
                }
            ),
            "city": forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "city",
                    "placeholder": "",
                    "required": "",
                }
            ),
        }

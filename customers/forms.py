from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Fieldset,
    Row,
    Column,
    Submit,
)

from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:

        model = Customer

        fields = [
            "user",
            "first_name",
            "last_name",
            "email",
            "mobile",
            "street",
            "address",
            "city",
            "postcode",
            "country",
        ]

        widgets = {

            "address": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }

    def __init__(
        self,
        *args,
        **kwargs,
    ):

        super().__init__(
            *args,
            **kwargs,
        )

        self.helper = FormHelper()

        self.helper.form_method = "post"

        self.helper.layout = [

            Fieldset(
                "Customer Information",

                Row(
                    Column(
                        "user",
                        css_class="col-md-12 mb-3",
                    ),
                ),

                Row(
                    Column(
                        "first_name",
                        css_class="col-md-6 mb-3",
                    ),

                    Column(
                        "last_name",
                        css_class="col-md-6 mb-3",
                    ),
                ),

                Row(
                    Column(
                        "email",
                        css_class="col-md-6 mb-3",
                    ),

                    Column(
                        "mobile",
                        css_class="col-md-6 mb-3",
                    ),
                ),
            ),

            Fieldset(
                "Address",

                "street",

                "address",

                Row(
                    Column(
                        "city",
                        css_class="col-md-5 mb-3",
                    ),

                    Column(
                        "postcode",
                        css_class="col-md-3 mb-3",
                    ),

                    Column(
                        "country",
                        css_class="col-md-4 mb-3",
                    ),
                ),
            ),

            Submit(
                "submit",
                "Save Customer",
                css_class="btn btn-primary",
            ),
        ]

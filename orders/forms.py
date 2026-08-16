from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Fieldset,
    Row,
    Column,
    Submit,
)

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:

        model = Order

        fields = [
            "customer",
            "product",
            "quantity",
            "status",
            "shipping_address",
        ]

        widgets = {

            "shipping_address": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),

            "quantity": forms.NumberInput(
                attrs={
                    "min": 1,
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
                "Order Information",

                Row(
                    Column(
                        "customer",
                        css_class="col-md-6 mb-3",
                    ),

                    Column(
                        "product",
                        css_class="col-md-6 mb-3",
                    ),
                ),

                Row(
                    Column(
                        "quantity",
                        css_class="col-md-4 mb-3",
                    ),

                    Column(
                        "status",
                        css_class="col-md-8 mb-3",
                    ),
                ),

                "shipping_address",
            ),

            Submit(
                "submit",
                "Save Order",
                css_class="btn btn-primary",
            ),
        ]

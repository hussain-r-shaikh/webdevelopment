from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Fieldset,
    Row,
    Column,
    Submit,
)

from .models import Payment


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            "order",
            "amount",
            "method",
            "status",
            "transaction_id",
        ]

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
                "Payment Information",

                "order",

                Row(
                    Column(
                        "amount",
                        css_class="col-md-4 mb-3",
                    ),

                    Column(
                        "method",
                        css_class="col-md-4 mb-3",
                    ),

                    Column(
                        "status",
                        css_class="col-md-4 mb-3",
                    ),
                ),

                "transaction_id",
            ),

            Submit(
                "submit",
                "Save Payment",
                css_class="btn btn-primary",
            ),
        ]

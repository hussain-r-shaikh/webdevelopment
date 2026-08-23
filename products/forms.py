from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Row,
    Column,
    Submit,
)


from .models import Product


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            "title",
            "description",
            "price",
            "image",
        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "min": "0",
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

        self.helper.form_enctype = (
            "multipart/form-data"
        )

        
        self.helper.layout = Layout(

            Fieldset(
                "Product",

                "title",

                "description",

                Row(
                    Column(
                        "price",
                        css_class="col-md-6 mb-3",
                    ),

                    Column(
                        "image",
                        css_class="col-md-6 mb-3",
                    ),
                ),

                Submit(
                "submit",
                "Create",
                css_class="btn btn-primary",
            ),
            ),       
        )

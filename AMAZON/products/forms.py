from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

from .models import Product


class ProductForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=Product.CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )

    class Meta:
        model = Product

        fields = [
            "name",
            "category",
            "description",
            "price",
            "image",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Product name",
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Product description",
                "rows": 5,
            }),

            "price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Price",
                "step": "0.01",
            }),

            "image": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_enctype = "multipart/form-data"

        self.helper.layout = Layout(
            Row(
                Column(
                    "name",
                    css_class="col-md-12",
                ),
            ),
            Row(
                Column(
                    "category",
                    css_class="col-md-6",
                ),

                Column(
                    "price",
                    css_class="col-md-6",
                ),

                css_class="g-3",
            ),

            Row(
                Column(
                    "description",
                    css_class="col-md-12",
                ),

                css_class="g-3",
            ),

            Row(
                Column(
                    "image",
                    css_class="col-md-12",
                ),
            ),

            Submit(
                "submit",
                "Save Product",
                css_class="btn btn-amazon mt-3",
            ),
        )

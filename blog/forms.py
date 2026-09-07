from django import forms
from django.contrib.auth.models import User
from .models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password", "password2"]

        widgets = {"address": forms.Textarea(attrs={"rows": 4}),
                   'dob': forms.DateInput(attrs={'type': 'date'}),
                   }

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get("password2"):
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.layout = Layout(
            Fieldset("",
            Row(Column("first_name", css_class="col-md-6"), 
                Column("last_name", css_class="col-md-6"), 
              ),
            Row(Column("username", css_class="col-md-6"),
                Column("email", css_class="col-md-6"),
                Column("password", css_class="col-md-6"), 
                Column("password2", css_class="col-md-6"), 
              ),
            ),
            Submit("submit", "Register", css_class="btn btn-warning"),
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")

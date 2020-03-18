from django import forms
from .models import UserInfo
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class SignUpForm(UserCreationForm):
# first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# mobile = forms.CharField(max_length=12)
# email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserInfo
        fields = ('first_name','last_name','email', 'mobile', 'password', )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('user','mobile','email',)

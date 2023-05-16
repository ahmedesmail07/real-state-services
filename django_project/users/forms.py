from django.contrib.auth.forms import UserCreationForm
from django import forms

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(required=True,max_length=300)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('full_name','email',)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

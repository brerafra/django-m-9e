from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class LoginForm(forms.Form):
    username = forms.CharField(
        label=_('Usuario'),
        validators=[username_validator],
        error_messages={'unique': _("Ya existe este usuario.")},
        widget=forms.TextInput(attrs={"class":"form-control"})
    )
    password = forms.CharField(label=_('Contraseña'),
                               widget=(forms.PasswordInput(attrs={'class':'form-control'})))
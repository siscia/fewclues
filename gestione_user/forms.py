from django.contrib.auth.models import User
from django import forms

attrs_dict = {'class': 'required'}

class RegistrationForm(forms.Form):
    """Il form per la registrazione, richiede un nick ed una password da ripetere"""
    nick = forms.RegexField(regex = r'^\w+$',
            max_length=30,
            widget=forms.TextInput(attrs=attrs_dict),
            label=("Username"),
            error_messages={'invalid': "This value must contain only letters, numbers and underscores."})
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
            label=("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict, render_value=False),
            label=("Password (again)"))

    def clean_nick(self):

        try:
            user = User.objects.get(username__iexact=self.cleaned_data['nick'])
        except User.DoesNotExist:
            return self.cleaned_data['nick']
        raise forms.ValidationError('Esiste gia un utente con questo nome, mi spiace')

    def clean(self):

        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields didn't match.")
        return self.cleaned_data


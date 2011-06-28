from django import forms

class formRisposta(forms.Form):
    risposta = forms.CharField()

    def clean_risposta(self):
        """Restituisce la risposta *pulita*"""
        return self.cleaned_data['risposta']

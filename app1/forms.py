from django import forms

class addCatForm(forms.Form):
    cat_name = forms.CharField(label='nom du chat', max_length=100)

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
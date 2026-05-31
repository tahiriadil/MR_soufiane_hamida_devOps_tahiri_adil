from django import forms
from .models import RendezVous
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

#le registre form poure cree un utilisateur
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#un form pour reservee un Rendez-vous et la method clean_date pour verifie la bon date
class RendezVousForm(forms.ModelForm):

    class Meta:
        model = RendezVous
        fields = ['service', 'date', 'heure']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("La date doit être future")
        return date
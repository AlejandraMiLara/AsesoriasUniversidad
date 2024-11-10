from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    matricula = forms.IntegerField(required=True, label="Matrícula")
    role = forms.IntegerField(required=True, label="Rol")

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('matricula', 'role')

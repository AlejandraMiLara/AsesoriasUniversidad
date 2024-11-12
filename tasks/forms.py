from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Asesoria

class CustomUserCreationForm(UserCreationForm):
    matricula = forms.IntegerField(required=True, label="Matrícula")
    role = forms.IntegerField(required=True, label="Rol")

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'matricula', 'role')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None 
        self.fields['password1'].help_text = None 
        self.fields['password2'].help_text = None
        for field_name, field in self.fields.items(): 
            field.widget.attrs['class'] = 'form-control'

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
            model = CustomUser
            fields = ('username', 'password')
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items(): 
            field.widget.attrs['class'] = 'form-control'

class AgregarAsesoriaForm(forms.ModelForm):
    class Meta:
        model = Asesoria
        fields = '__all__'

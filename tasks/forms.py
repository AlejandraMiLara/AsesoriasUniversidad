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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AgregarAsesoriaForm, self).__init__(*args, **kwargs)
        if user.role == 0: 
            #estudiante hace request
            self.fields['estudiante'].queryset = CustomUser.objects.filter(role=0, username=user.username)
            self.fields['profe'].queryset = CustomUser.objects.filter(role=1)
        else:
            #profesor hace request
            self.fields['profe'].queryset = CustomUser.objects.filter(role=1, username=user.username)
            self.fields['estudiante'].queryset = CustomUser.objects.filter(role=0)
        

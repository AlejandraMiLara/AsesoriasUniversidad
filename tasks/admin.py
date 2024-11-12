from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Materia, MateriasProfes, Asesoria
from .forms import AgregarAsesoriaForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('matricula', 'role')}),
    )

class AsesoriaAdmin(admin.ModelAdmin):
    class Meta:
        model = Asesoria
        fields = '__all__'


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Materia)
admin.site.register(MateriasProfes)
admin.site.register(Asesoria, AsesoriaAdmin)


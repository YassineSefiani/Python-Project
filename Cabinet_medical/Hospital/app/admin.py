from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import Patient

class ProclinicAdminSite(admin.AdminSite):
    site_header = 'Proclinic Administration'
    site_title = 'Proclinic Admin'
    index_title = 'Welcome to Proclinic Administration'

proclinic_admin_site = ProclinicAdminSite(name='proclinic_admin')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'date_of_birth', 'age', 'phone', 'email', 'gender', 'address', 'edit_link')
    search_fields = ('patient_name', 'email')
    list_filter = ('gender', 'date_of_birth')

    def edit_link(self, obj):
        return format_html('<a href="{}">Edit</a>', reverse('proclinic_admin:app_patient_change', args=[obj.pk]))
    edit_link.short_description = 'Edit'
    edit_link.allow_tags = True

# Enregistrer les modèles avec le site d'administration personnalisé
proclinic_admin_site.register(Patient, PatientAdmin)
proclinic_admin_site.register(User, UserAdmin)
proclinic_admin_site.register(Group, GroupAdmin)


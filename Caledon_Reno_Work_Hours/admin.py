from django.contrib import admin
from .models import FilledForm, Application, Estimate, Job
from django.contrib.auth.models import User
from import_export.admin import ExportActionMixin


class ImportAdmin(ExportActionMixin, admin.ModelAdmin):
    site_header = "Export Admin"


class HRAdminSite(admin.AdminSite):
    site_header = "HR admin"
    site_title = "HR admin"


hr_admin_site = HRAdminSite(name='hr_admin')


hr_admin_site.register(User)
admin.site.register(FilledForm, ImportAdmin)
# admin.site.register(Application)
# admin.site.register(Estimate)
# admin.site.register(Job)
# Register your models here.

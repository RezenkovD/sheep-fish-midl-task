from django.contrib import admin

from api.models import Printer, Check

# Register your models here.

admin.site.register(Printer)


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_filter = ("printer_id", "type", "status")

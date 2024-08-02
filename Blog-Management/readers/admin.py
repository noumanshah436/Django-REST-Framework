from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Reader, MarkAsRead


# Register your models here.

@admin.register(Reader)
class ReaderAdmin(ImportExportModelAdmin):
    pass


@admin.register(MarkAsRead)
class MarkAsReadAdmin(ImportExportModelAdmin):
    pass

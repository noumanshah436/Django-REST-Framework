from __future__ import unicode_literals
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from utility.models import Region, Gender, Difficulty, EmailVerification
from import_export import resources


# Register your models here.

@admin.register(Difficulty)
class DifficultyAdmin(ImportExportModelAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(ImportExportModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(ImportExportModelAdmin):
    pass


@admin.register(EmailVerification)
class EmailVerificationAdmin(ImportExportModelAdmin):
    pass
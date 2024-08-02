from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import BlogPost


# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(ImportExportModelAdmin):
    pass

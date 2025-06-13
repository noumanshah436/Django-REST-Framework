from django.contrib import admin
from api.models import Session, Message, Document


# Register your models here.
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('hash_id', 'user')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'content', 'reply')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('session', 'file_name', 'file_id')

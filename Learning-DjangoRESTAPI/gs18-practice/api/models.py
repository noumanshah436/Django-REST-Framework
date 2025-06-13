from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Models for Socket Commmunication

class Random(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255, blank=True, null=True)


class Queue(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.IntegerField()


class Session(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="sessions")
    hash_id = models.CharField(max_length=255, editable=False, unique=True)
    goal = models.TextField(blank=True, null=True)
    barriers = models.TextField(blank=True, null=True)
    enablers = models.TextField(blank=True, null=True)
    commitments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Session {self.hash_id}"


class Message(models.Model):
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    reply = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Message in Session {self.session.id} at {self.timestamp}"


class Document(models.Model):
    session = models.ForeignKey(
        'Session',
        on_delete=models.CASCADE,
        related_name='documents',
    )
    file_name = models.CharField(max_length=255)
    file_id = models.CharField(max_length=255, unique=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

import uuid
from rest_framework import serializers
from .models import Session, Message, Document


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'reply', 'timestamp']


class SessionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = [
            'id', 'hash_id', 'goal', 'barriers', 'enablers', 'commitments', 'created_at', 'updated_at', 'messages'
        ]
        read_only_fields = ['id', 'hash_id', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        validated_data['hash_id'] = str(uuid.uuid4())
        print(f"validated_data ------------------- {validated_data}")
        return super().create(validated_data)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'session', 'file_name', 'file_id', 'uploaded_at']

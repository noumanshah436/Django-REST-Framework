import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from api.models import Session, Message, Document
from api.serializers import SessionSerializer, MessageSerializer, DocumentSerializer


User = get_user_model()

# Here’s the list of all available URLs:

# http://127.0.0.1:8000/api/v1/sessions/
# http://127.0.0.1:8000/api/v1/sessions/<hash_id>/
# http://127.0.0.1:8000/api/v1/sessions/<hash_id>/upload-document/
# http://127.0.0.1:8000/api/v1/sessions/<hash_id>/documents/
# http://127.0.0.1:8000/api/v1/sessions/<hash_id>/messages/


# username: admin
# password: admin
# email: admin@example.com


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    lookup_field = 'hash_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Session.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser], url_path='upload-document')
    def upload_document(self, request, hash_id=None):
        try:
            session = self.get_object()
            file = request.FILES['file']
            file_name = file.name

            logging.info(f"Received file: {file_name}")

            if 'collection_name' in request.POST:
                collection_name = request.POST['collection_name']
            else:
                collection_name = 'basic_vppl'

            data = {
                'session': session.id,
                'file_name': file_name,
                'file_id': "dummy file id"
            }
            serializer = DocumentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                {
                    'file_name': file_name, 'file_id': f'{mongo_file_id}'
                }, status=200
            )

        except KeyError as e:
            logging.error(f"KeyError: {e}")
            return Response({'error': 'No file part in the request'}, status=400)
        except ValueError as e:
            logging.error(f"ValueError: {e}")
            return Response({'error': f'Unsupported file type: {e}'}, status=400)
        except Exception as e:
            logging.error(f"Exception: {str(e)}")
            return Response({'error': f'{e}'}, status=500)

    @action(detail=True, methods=['get'], url_path='documents')
    def get_documents(self, request, hash_id=None):
        try:
            session = self.get_object()
            documents = session.documents.all()

            files = []
            for document in documents:
                file_id = ObjectId(document.file_id)
                grid_out = fs.get(file_id)
                file_content = grid_out.read()

                files.append({
                    'file_name': document.file_name,
                    'file_content': file_content.decode('utf-8', errors='ignore'),
                    'uploaded_at': document.uploaded_at
                })

            return Response(files, status=200)

        except Exception as e:
            logging.error(f"Error in getting file: {e}")
            return Response({'error': f'Error in getting file: {e}'}, status=500)

    def retrieve(self, request, *args, **kwargs):
        hash_id = kwargs.get('hash_id')
        session = self.get_queryset().filter(hash_id=hash_id).first()

        if session:
            serializer = self.get_serializer(session)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, *args, **kwargs):
        session = self.get_object()
        serializer = self.get_serializer(
            session, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='messages')
    def get_messages(self, request, hash_id=None):
        try:
            session = self.get_object()
            messages = session.messages.all()
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            error_message = f"Error fetching messages for session {
                hash_id}: {e}"
            logging.error(error_message)
            return Response({'error': error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

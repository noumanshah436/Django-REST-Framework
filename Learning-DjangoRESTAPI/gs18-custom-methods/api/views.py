from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset


class StudentModelViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Custom method examples

    # GET http://127.0.0.1:8000/studentapi/top_students/
    @action(detail=False, methods=['get'], url_path='top_students',)
    def top_students(self, request):
        """
        A custom endpoint to retrieve top-performing students.
        """
        # Example logic: Filter students with roll numbers < 10
        top_students = Student.objects.filter(roll__lt=3)
        serializer = self.get_serializer(top_students, many=True)
        return Response(serializer.data)

    # POST http://127.0.0.1:8000/studentapi/1/update_city/
    @action(detail=True, methods=['post'])
    def update_city(self, request, pk=None):
        """
        A custom endpoint to update the city of a specific student.
        """
        student = self.get_object()  # Get the current student instance
        city = request.data.get('city')
        if city:
            student.city = city
            student.save()
            return Response({'message': 'City updated successfully'})
        return Response({'error': 'City not provided'}, status=400)

    # POST http://127.0.0.1:8000/studentapi/1/update_name/

    @action(detail=True, methods=['post'], url_path='update_name')
    def update_name(self, request, pk=None):
        """
        A custom endpoint to update the city of a specific student.
        URL: /studentapi/update_city/<id>/
        """
        student = self.get_object()  # Get the current student instance
        name = request.data.get('name')
        if name:
            student.name = name
            student.save()
            return Response({'message': 'Student name updated successfully'})
        return Response({'error': 'name not provided'}, status=400)

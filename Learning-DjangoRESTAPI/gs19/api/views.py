from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets


# ReadOnlyModelViewSet
# The ReadOnlyModelViewSet class also inherits from GenericAPIView.
# As with ModelViewSet it also includes implementations for various actions,
# but unlike ModelViewSet only provides the 'read-only' actions, .list() and .retrieve().


class StudentReadOnlyModelViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

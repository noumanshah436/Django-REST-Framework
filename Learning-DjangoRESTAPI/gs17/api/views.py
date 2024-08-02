from .models import Student
from .serializers import StudentSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/viewsets/

# ViewSet
# A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(),
# and instead provides actions such as .list() and .create().

# The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using 
# the .as_view() method.

# Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a 
# router class, that automatically determines the urlconf for you.

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("***********List************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        print("***********Retrieve************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        print("***********Create************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        if serializer.is_valid():
            serializer.save()
            res = {"Message": "Data Created Successfully"}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("***********Update************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {"Message": "Data Updated Successfully"}
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def partial_update(self, request, pk):
        print("***********Partial Update************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {"Message": "Partial Data Updated Successfully"}
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def destroy(self, request, pk):
        print("***********Destroy************")
        print("Basename: ", self.basename)
        print("Action: ", self.action)
        print("Detail: ", self.detail)
        print("Suffix: ", self.suffix)
        print("Name: ", self.name)
        print("Description: ", self.description)
        stu = Student.objects.get(id=pk)
        stu.delete()
        res = {"Message": "Data Deleted Successfully"}
        return Response(res, status=status.HTTP_200_OK)

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'Message': 'Helo World'})

# @api_view(['GET'])     # same as above
# def hello_world(request):
#     return Response({'Message': 'Helo World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == "POST":
#         print(request.data)
#         return Response({'Message': 'This is POST request'})


@api_view(["GET", "POST"])
def hello_world(request):
    if request.method == "GET":
        return Response({"Message": "Helo!! This is a GET request"})

    if request.method == "POST":
        print("POST DATA: ", request.data)
        return Response({"Message": "This is POST request", "data": request.data})


# http://localhost:8000/studentapi/

# Pass this json data as content for POST request
# {"name": "Ohit", "roll": 16, "city": "Ranchi"}

import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer


def home(request, *args, **kwargs):
    body = request.body  # byte string of json data
    print(body)  # b'{"name": "Nouman"}'

    print("request.GET")  # url query params
    print(request.GET)  # <QueryDict: {'abc': ['123']}>

    data = {}
    try:
        # convert string of json data to python dictionary
        data = json.loads(body)
    except Exception as e:
        print("error", e.message)
    finally:
        pass

    return JsonResponse(data)


def model_instance_to_dic(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "price"])
    return JsonResponse(data)


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)

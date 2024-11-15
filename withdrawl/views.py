from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Requests
from .serializers import RequestsSerializers

# Create your views here.
@api_view(['POST'])
def post_request(request):
    serializer = RequestsSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_request(request):
    requests = Requests.objects.all()
    serializer = RequestsSerializers(requests, many=True)
    return Response(serializer.data)
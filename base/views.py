from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.


@api_view(['GET'])
def endPoint(request):
    data = ['/advocates', 'advocates/:username']
    return Response(data)

@api_view(['GET'])
def AdvocatesList(request):
    query = request.GET.get('query')

    if query != None:
        query = ''

    advocate = Advocates.objects.filter(username__contains=query)
    serializer = AdvocateSerializer(advocate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AdvocateDetails(request, username):
    advocate = Advocates.objects.get(username=username)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)
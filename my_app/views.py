from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import models
from . import serializers


@api_view(['POST', 'GET'])
def create_category(request):
    if request.method == 'POST':
        serializer = serializers.CategorySerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerialize(instance=categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request, pk):
    category = generics.get_object_or_404(models.Category, pk=pk)
    if request.method == 'GET':
        serializer = serializers.CategorySerialize(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = serializers.CategorySerialize(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_company(request):
    if request.method == 'POST':
        serializer = serializers.CompanySerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        companies = models.Company.objects.all()
        serializer = serializers.CompanySerialize(instance=companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_company(request, pk):
    company = generics.get_object_or_404(models.Company, pk=pk)
    if request.method == 'GET':
        serializer = serializers.CompanySerialize(instance=company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = serializers.CompanySerialize(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST', 'GET'])
def create_good(request):
    if request.method == 'POST':
        serializer = serializers.GoodSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        goods = models.Good.objects.all()
        serializer = serializers.GoodSerialize(instance=goods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_good(request, pk):
    good = generics.get_object_or_404(models.Good, pk=pk)
    if request.method == 'GET':
        serializer = serializers.GoodSerialize(instance=good)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = serializers.GoodSerialize(instance=good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


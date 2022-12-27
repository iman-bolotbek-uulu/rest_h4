from rest_framework import serializers
from . import models


class CompanySerialize(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    office = serializers.CharField(max_length=30)

    def create(self, validated_data):
        company = models.Company.objects.create(
            name=validated_data['name'],
            office=validated_data['office'],
        )
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.office = validated_data['office']
        instance.save()
        return instance


class CategorySerialize(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        category = models.Category.objects.create(
            name=validated_data['name'],
        )
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class GoodSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    price = serializers.IntegerField()
    company = serializers.IntegerField()
    category = serializers.IntegerField()

    def create(self, validated_data):
        good = models.Good.objects.create(
            name=validated_data['name'],
            price=validated_data['price'],
            company=validated_data['company'],
            category=validated_data['category'],
        )
        return good

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.company = validated_data['company']
        instance.category = validated_data['category']
        instance.save()
        return instance

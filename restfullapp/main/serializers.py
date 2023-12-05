from .models import *
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ListOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfWork
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderList
        fields = '__all__'

from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *


class CarApiView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarViewDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDelete(generics.DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdate(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# //////////////////////////////////////////#

class ClientApiView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientViewDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDelete(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdate(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# //////////////////////////////////////////#

class WorkerApiView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerViewDetail(generics.RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerCreate(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerDelete(generics.DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerUpdate(generics.UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


# //////////////////////////////////////////#

class ListOfWorkApiView(generics.ListAPIView):
    queryset = ListOfWork.objects.all()
    serializer_class = ListOfWorkSerializer


class ListOfWorkViewDetail(generics.RetrieveAPIView):
    queryset = ListOfWork.objects.all()
    serializer_class = ListOfWorkSerializer


class ListOfWorkCreate(generics.CreateAPIView):
    queryset = ListOfWork.objects.all()
    serializer_class = ListOfWorkSerializer


class ListOfWorkDelete(generics.DestroyAPIView):
    queryset = ListOfWork.objects.all()
    serializer_class = ListOfWorkSerializer


class ListOfWorkUpdate(generics.UpdateAPIView):
    queryset = ListOfWork.objects.all()
    serializer_class = ListOfWorkSerializer


# //////////////////////////////////////////#


class OrderListApiView(generics.ListAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderListViewDetail(generics.RetrieveAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderListCreate(generics.CreateAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderListDelete(generics.DestroyAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer


class OrderListUpdate(generics.UpdateAPIView):
    queryset = OrderList.objects.all()
    serializer_class = OrderListSerializer

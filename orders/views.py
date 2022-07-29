from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import OrderSerializer, OrderDetailSerializer, OrderUpdateSerializer
from .models import Orders
from rest_framework.permissions import IsAuthenticated

class OrderCreateListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Orders.objects.all()
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data=request.data
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Orders.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        serializer= self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class  UpdateOrderStatus(UpdateAPIView):
    serializer_class = OrderUpdateSerializer
    queryset = Orders.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserOrderView(ListAPIView):
    serializer_class = OrderDetailSerializer
    def get(self, request):
        user = request.user
        orders = Orders.objects.all().filter(user=user)
    
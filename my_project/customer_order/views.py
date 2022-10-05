from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CustomerOrder
from .serializers import CustomerOrderSerializer

class CustomerOrderApiView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    # get all orders
    def get(self, request, *args, **kwargs):
        '''
        List all customer orders
        '''
        orders = CustomerOrder.objects.all()
        serializer = CustomerOrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # add new order
    def post(self, request, *args, **kwargs):
        '''
        Create the Orders with given data
        '''
        data = {
            'description': request.data.get('description'), 
            'item_count': request.data.get('item_count'), 
            'order_created_date': request.data.get('order_created_date'),
            'customer': request.data.get('customer_id')
        }
        serializer = CustomerOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerOrderDetailApiView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, customer_order_id):
        '''
        Helper method to get the customer order object with given id
        '''
        try:
            return CustomerOrder.objects.get(customer_order_id=customer_order_id)
        except Customer.DoesNotExist:
            return None


    # Get the customer order given by the ID
    def get(self, request, id, *args, **kwargs):
        '''
        Retrieves the Customer Order with given id
        '''
        order_instance = self.get_object(id)
        if not order_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerOrderSerializer(order_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    #  Edit customer order given by the ID
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the customer order item with given id if exists
        '''
        order_instance = self.get_object(id)
        if not order_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'description': request.data.get('description'), 
            'item_count': request.data.get('item_count'), 
            'order_created_date': request.data.get('order_created_date'),
            'customer': request.data.get('customer_id')
        }
        serializer = CustomerOrderSerializer(instance = order_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #  Delete customer order given by the ID
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the customer order item with given id if exists
        '''
        order_instance = self.get_object(id)
        if not order_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        order_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
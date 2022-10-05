from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Customer
from .serializers import CustomerSerializer

class CustomerApiView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    # get all customers
    def get(self, request, *args, **kwargs):
        '''
        List all customers
        '''
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # add new customer
    def post(self, request, *args, **kwargs):
        '''
        Create the Customer with given data
        '''
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'date_of_birth': request.data.get('date_of_birth'),
            'currency_balance': request.data.get('currency_balance'),
            'page_visitis': request.data.get('page_visitis')
        }
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailApiView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, customer_id):
        '''
        Helper method to get the customer object with given id
        '''
        try:
            return Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return None


    # Get the customer given by the ID
    def get(self, request, id, *args, **kwargs):
        '''
        Retrieves the Customer with given id
        '''
        customer_instance = self.get_object(id)
        if not customer_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CustomerSerializer(customer_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    #  Edit customer given by the ID
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the customer item with given id if exists
        '''
        customer_instance = self.get_object(id)
        if not customer_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'first_name': request.data.get('first_name'), 
            'last_name': request.data.get('last_name'), 
            'date_of_birth': request.data.get('date_of_birth'),
            'currency_balance': request.data.get('currency_balance'),
            'page_visitis': request.data.get('page_visitis')
        }
        serializer = CustomerSerializer(instance = customer_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #  Delete customer given by the ID
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the customer item with given id if exists
        '''
        customer_instance = self.get_object(id)
        if not customer_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        customer_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
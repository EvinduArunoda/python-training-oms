from unicodedata import category
from django.shortcuts import render

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Item
from category.models import Category
from .serializers import ItemSerializer

class ItemApiView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # get all items
    def get(self, request, *args, **kwargs):
        '''
        List all/filtered items
        '''
        name = request.GET.get('category')
        if name != '' and name != None:
            try:
                category = Category.objects.get(name=name)
                items = Item.objects.filter(category=category.category_id)
            except Category.DoesNotExist:
                category = None
                items = []
        else:
            items = Item.objects.all()
            
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # add new item
    def post(self, request, *args, **kwargs):
        '''
        Create the Item with given data
        '''
        data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'visible': request.data.get('visible'),
            'price': request.data.get('price')
        }
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetailApiView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, item_id):
        '''
        Helper method to get the item object with given id
        '''
        try:
            return Item.objects.get(item_id=item_id)
        except Item.DoesNotExist:
            return None


    # Get the item given by the ID
    def get(self, request, id, *args, **kwargs):
        '''
        Retrieves the Item with given id
        '''
        item_instance = self.get_object(id)
        if not item_instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ItemSerializer(item_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    #  Edit item given by the ID
    def put(self, request, id, *args, **kwargs):
        '''
        Updates the item with given id if exists
        '''
        item_instance = self.get_object(id)
        if not item_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'), 
            'description': request.data.get('description'), 
            'visible': request.data.get('visible'),
            'price': request.data.get('price')
        }
        serializer = ItemSerializer(instance = item_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #  Delete item given by the ID
    def delete(self, request, id, *args, **kwargs):
        '''
        Deletes the item with given id if exists
        '''
        item_instance = self.get_object(id)
        if not item_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        item_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class ItemToggleVisibilityApiView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, item_id):
        '''
        Helper method to get the item object with given id
        '''
        try:
            return Item.objects.get(item_id=item_id)
        except Item.DoesNotExist:
            return None

    # toggle visibility
    def post(self, request, id, *args, **kwargs):
        '''
        Toggle visibility of the given Item
        '''

        item_instance = self.get_object(id)
        if not item_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'visible': not(item_instance.visible)
        }
        serializer = ItemSerializer(instance = item_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemFilteredByCategoryApiView(APIView):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # get all items
    def get(self, request, *args, **kwargs):
        name = request.GET.get('category')
        '''
        List all items
        '''
        # print(category)
        customers = Item.objects.all()
        serializer = ItemSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

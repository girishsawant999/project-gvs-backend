from django.shortcuts import render

# Create your views here.
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .validations import create_customer


class Customer(APIView):
    """
    API related with the customer.
    """

    @staticmethod
    def post(request):
        try:
            print("In Post")
            customer = create_customer(request.data)
            customer.save()
            return Response(
                data={'is_success': True, 'message': 'successfully created user', 'data': customer.customer_id},
                status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                data={'is_success': False, 'message': str(err), 'data': ''},
                status=status.HTTP_200_OK)

    @staticmethod
    def get(request):
        pass

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass

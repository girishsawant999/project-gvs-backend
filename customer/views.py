from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers

from customer import messages
from customer.models import CustomerModel
from customer.serializers import CustomerModelGetSerializer
from customer.validation import customer_create


class CustomerView(APIView):
    """
    :Summary:
        Api related to customer model
    """

    @staticmethod
    def post(request):
        data = request.data
        try:
            customer = customer_create(data)
            customer.save()
            return Response(
                data={"is_success": True, "message": messages.created_success, "data": customer.customer_id},
                status=status.HTTP_201_CREATED)
        except Exception as err:
            return Response(
                data={"is_success": False, "message": messages.something_went_wrong, "data": ''},
                status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        customer_id = request.query_params['customer_id']
        try:
            customer = CustomerModelGetSerializer(CustomerModel.objects.get(customer_id=customer_id)).data
            message = messages.data_found
        except CustomerModel.DoesNotExist:
            customer = []
            message = messages.data_not_found
        return Response(
            data={"is_success": True, "message": message, "data": customer},
            status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        pass

    @staticmethod
    def delete(request):
        pass

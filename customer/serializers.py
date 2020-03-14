from rest_framework import serializers

from customer.models import CustomerModel


class CustomerModelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ("customer_id", "first_name", "last_name", "gender", "email", "contact_no", "city", "state",
                  "address_line1", "address_line2", "pin_code", "last_seen")

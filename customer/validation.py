import uuid

from customer.models import CustomerModel


def customer_create(data):
    customer = CustomerModel(
        customer_id=uuid.uuid4(),
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        gender=data.get('gender'),
        email=data.get('email'),
        contact_no=data.get('contact_no'),
        city=data.get('city'),
        state=data.get('state'),
        address_line1=data.get('address_line1'),
        address_line2=data.get('address_line2'),
        pin_code=data.get('pin_code'),
    )
    return customer



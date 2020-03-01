from datetime import datetime

from .models import Customers


def create_customer(data):
    try:
        customer = Customers(
            updated_at=datetime.now(),
            first_name=data.get('first_name').capitalize(),
            last_name=data.get('last_name').capitalize(),
            gender=data.get('gender'),
            email=data.get('email'),
            contact_no=data.get('contact_no'),
            city=data.get('city').capitalize(),
            state=data.get('state').capitalize(),
            address_line1=data.get('address_line1').capitalize(),
            address_line2=data.get('address_line2').capitalize(),
        )
    except Exception as err:
        print("Exception--",err)
    return customer

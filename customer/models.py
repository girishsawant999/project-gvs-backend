from django.db import models


# Create your models here.
class CustomerModel(models.Model):
    """
    :Summary:
        Customer database model.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer_id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    gender = models.TextField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = models.TextField(max_length=50)
    contact_no = models.TextField(max_length=10)
    city = models.TextField(max_length=20)
    state = models.TextField(max_length=20)
    address_line1 = models.TextField(max_length=40)
    address_line2 = models.TextField(max_length=30, null=True)
    pin_code = models.TextField(max_length=6)
    last_seen = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.customer_id

from django.db import models


# Create your models here.
class Customers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    customer_id = models.UUIDField(primary_key=True)
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    gender = models.TextField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    email = models.EmailField()
    contact_no = models.TextField(max_length=10)
    city = models.TextField(max_length=20)
    state = models.TextField(max_length=20)
    address_line1 = models.TextField(max_length=40)
    address_line2 = models.TextField(max_length=40, null=True)
    last_seen = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.customer_id

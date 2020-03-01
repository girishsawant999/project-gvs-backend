from django.urls import path, include

from customer import views

urlpatterns = [
 path('', views.Customer.as_view(),name='customer'),
]
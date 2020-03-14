from django.urls import path

from customer import views

urlpatterns = [
    path('', views.CustomerView.as_view(), name='customer_model')
]

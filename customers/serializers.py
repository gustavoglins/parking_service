from rest_framework import serializers

from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        moodel = Customer
        fields = "__all__"

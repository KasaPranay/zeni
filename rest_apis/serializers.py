from rest_framework import serializers
from .models import DBase

class DBaseserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DBase
        fields = ('FirstName','LastName','password','email')


from rest_framework import serializers
from .models import Account


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        read_only_fields = ["id"]
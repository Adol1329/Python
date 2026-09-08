from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "user_type",
            "password",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

        extra_kwargs = {
            "password": {
                "write_only": True,
                "min_length": 8,
            }
        }

    # -------------------------
    # FIRST NAME VALIDATION
    # -------------------------

    def validate_first_name(self, value):

        if not value.isalpha():
            raise serializers.ValidationError(
                "First name must contain letters only."
            )

        return value


    def validate_last_name(self, value):

        if not value.isalpha():
            raise serializers.ValidationError(
                "Last name must contain letters only."
            )

        return value


    def validate_phone_number(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain digits only."
            )

        if not value.startswith("07"):
            raise serializers.ValidationError(
                "Phone number must start with 07."
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return value

   

    def validate_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError(
                "Password must contain at least 8 characters."
            )

        return value

   

def create(self, validated_data):

    password = validated_data.pop("password")

    user = User.objects.create_user(
        password=password,
        **validated_data)
    return user
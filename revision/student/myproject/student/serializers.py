from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ["id"]

def validate_department(self, department):
    if not department:
        raise serializers.ValidationError(
            "Department is required."
        )

    return department


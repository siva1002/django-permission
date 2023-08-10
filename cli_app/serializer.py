from .models import (Users)
from rest_framework.serializers import ModelSerializer, ValidationError, Serializer, SerializerMethodField

class UserSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields="__all__"
        read_only_fields =['last_login',"is_superuser","is_active","is_admin"]

    def create(self, validated_data):
        user = Users.objects.create(**validated_data)
        user.user_permissions.set(validated_data.get('user_permissions'))
        print(user.has_perm("Todo_app.view_todo"),"permissions")
        return user

        
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotAuthenticated

from core.models import User


class PasswordField(serializers.CharField):
    def __init__(self, **kwargs):
        kwargs["style"] = {"input_type": "password"}
        kwargs.setdefault("write_only", True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password", "password_repeat")

    def validate(self, attrs: dict):
        if attrs["password"] != attrs["password_repeat"]:
            raise ValidationError("Password must match")
        return attrs

    def create(self, validated_data: dict):
        del validated_data["password_repeat"]
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate_username(self, value):
        """Ensure username exists"""
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError(["User with such username doesn't exist"])
        return value


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class UpdatePasswordSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    old_password = PasswordField(required=True)
    new_password = PasswordField(required=True)

    def validate(self, attrs: dict):
        if not (user := attrs["user"]):
            raise NotAuthenticated
        if not user.check_password(attrs["old_password"]):
            raise ValidationError({"old password": "field is incorrect"})
        return attrs

    def create(self, validated_data: dict) -> User:
        raise NotImplementedError

    def update(self, instance: User, validated_data: dict) -> User:
        instance.password = make_password(validated_data["new_password"])
        instance.save(update_fields=("password",))
        return instance

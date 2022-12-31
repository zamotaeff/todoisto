from django.contrib.auth.hashers import make_password

from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate

USER_MODEL = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_repeat = serializers.CharField(write_only=True)

    def create(self, validated_data) -> USER_MODEL:
        password = validated_data.get('password')
        # delete pass repeat from validated_data dict and return value
        password_repeat = validated_data.pop('password_repeat')

        # Validate password
        if password != password_repeat:
            raise serializers.ValidationError('Password do not match.')

        hashed_password = make_password(password)
        validated_data['password'] = hashed_password
        instance = super().create(validated_data)

        return instance

    class Meta:
        model = USER_MODEL
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def create(self, validated_data):
        user = authenticate(
            usernanme=validated_data['username'],
            password=validated_data['password']
        )
        if not user:
            raise exceptions.AuthenticationFailed

        return user

    class Meta:
        model = USER_MODEL
        fields = ['username', 'password']


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = "__all__"


class UpdatePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = USER_MODEL
        fields = "__all__"

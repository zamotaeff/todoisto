from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from django.contrib.auth import get_user_model


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

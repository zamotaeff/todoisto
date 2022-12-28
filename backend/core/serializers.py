from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField()

    def create(self, validated_data):
        # Validate password
        if validated_data.get('password') != validated_data.get('password_repeat'):
            raise ValidationError('Пароли не совпадают')
        if not validate_password(validated_data.get('password')):
            user = User.objects.create(**validated_data)

            # Set password into a hash and save
            user.set_password(validated_data.get('password'))

            user.save()

            return user

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'password_repeat', ]


class UserLoginSerializer(serializers.ModelSerializer):

    def post(self):
        print(self.validated_data)

    class Meta:
        model = User
        fields = ['username', 'password']

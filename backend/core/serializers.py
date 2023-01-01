from django.contrib.auth.hashers import make_password

from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model, authenticate, password_validation

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
        #
        # try:
        #     password_validation.validate_password(password)
        # except Exception as ex:
        #     raise serializers.ValidationError(ex)

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
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class UpdatePasswordSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = attrs['user']
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({'old_password': 'incorrect password'})
        return attrs

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data['new_password'])
        instance.save()

        return instance

    class Meta:
        model = USER_MODEL
        fields = "__all__"

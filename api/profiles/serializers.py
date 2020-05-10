from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    ValidationError,
    HyperlinkedIdentityField,
)
from .models import Profile


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'bio',
            'birth_date',
            'location'
        ]

    def validate_birth_date(self, birth_date):
        if birth_date:
            if birth_date > timezone.now().date():
                raise ValidationError("Birth date can not be a future date.")

        return birth_date


class UserListCreateSerializer(ModelSerializer):
    edit_profile = HyperlinkedIdentityField(view_name='user-api-detail')
    profile = ProfileSerializer(read_only=True)
    password = CharField(min_length=8, max_length=100, write_only=True,
                         style={'input_type': 'password'})
    confirm_password = CharField(min_length=8, max_length=100, write_only=True,
                                 style={'input_type': 'password'})

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'profile',
            'edit_profile',
        ]
        extra_kwargs = {
            'email': {'read_only': True},
            'first_name': {'read_only': True},
            'last_name': {'read_only': True}
        }

    def validate_confirm_password(self, value):
        data = self.get_initial()
        password = data.get("password")
        confirm_password = value
        if password != confirm_password:
            raise ValidationError("Passwords must match.")

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username, password=password)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj


class UserDetailSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile']

    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile_data = validated_data.pop('profile')
        profile = instance.profile

        profile.bio = profile_data.get(
            'bio',
            profile.bio
        )
        profile.birth_date = profile_data.get(
            'birth_date',
            profile.birth_date
        )
        profile.location = profile_data.get(
            'location',
            profile.location
        )
        profile.save()

        return instance

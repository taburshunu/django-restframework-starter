from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    displayname = serializers.CharField(
        style={'placeholder': 'Add display name'}
    )
    info = serializers.CharField(
        required=False,
        allow_blank=True,
        style={'placeholder': 'Add information', 'rows': 3}
    )
    image = serializers.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['image', 'displayname', 'info']

class EmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['email']

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
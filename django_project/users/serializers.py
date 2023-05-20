from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class CustomUserDetailsSerializer(UserDetailsSerializer):
    username = serializers.CharField(max_length=150,read_only=True)
    email = serializers.CharField(max_length=150,read_only=True)
    first_name = serializers.CharField(max_length=20, required=False)
    last_name = serializers.CharField(max_length=20, required=False)
    class Meta :
        model = UserModel
        fields = ('username','email','first_name','last_name')
        read_only_fields = ('email','username')

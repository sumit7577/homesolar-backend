from rest_framework import serializers
from django.conf import settings
from app.models import *
from django.contrib.auth import get_user_model

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"
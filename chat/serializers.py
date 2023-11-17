from rest_framework import serializers
from .models import UserProfile, Message, Chat

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'profile_pic']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']

class ChatListSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ['chat_id', 'participants']
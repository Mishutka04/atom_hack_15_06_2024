from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Prompt, Dialog, Message, QuestionAnswer, Like, Dislike
import random


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined'
            ]

class PromptSerializer(serializers.ModelSerializer):
    requests_count = serializers.SerializerMethodField()
    class Meta:
        model = Prompt
        fields = [
            'id',
            'title',
            'text',
            'likes_count',
            'dislikes_count',
            'requests_count'
            ]
        
    def get_requests_count(self, obj):
        delta = random.randint(100, 200)
        # delta = 100
        result = obj.likes.count() + obj.dislikes.count() + delta
        return result

class DialogSerializer(serializers.ModelSerializer):
    user = serializers.ImageField(read_only = True)
    class Meta:
        model = Dialog
        fields = [
            'id',
            'user',
            'prompt', 
            'created_at'
            ]

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'id',
            'dialog',
            'text',
            'is_user_message',
            'timestamp'
            ]

class DialogDetailSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    prompt = PromptSerializer(read_only=True)
    class Meta:
        model = Dialog
        fields = [
            'id',
            'prompt',
            'created_at',
            'messages'
            ]


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = [
            'id',
            'question',
            'answer'
            ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'
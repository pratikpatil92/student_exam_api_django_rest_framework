from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'is_staff')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
            'is_staff': {
                'read_only':True,
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            # is_staff=validated_data['is_staff'],
        )

        return user


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quenstions
        fields = ('id', 'question', 'question_type', 'choice_one', 'choice_two', 'choice_three', 'choice_four')


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answers
        fields = ('user','questions', 'answer', 'image_ans', 'submited')


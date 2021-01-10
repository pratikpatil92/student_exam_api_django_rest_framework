from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin
from rest_framework import generics

from .serializers import *
from .models import *
from .mypaginations import *


class UserProfileView(viewsets.ModelViewSet):
    """View for create new user and get all user"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)


class AllUser(generics.ListAPIView):
    """List all user except admin user"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('is_staff',)


class OneUserById(generics.RetrieveAPIView):
    """get one user data by id"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PostQuestions(generics.CreateAPIView):
    """Post question"""
    serializer_class = QuestionSerializer
    queryset = Quenstions.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateQuenstions(generics.UpdateAPIView):
    """Post question"""
    serializer_class = QuestionSerializer
    queryset = Quenstions.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class AllQuenstions(generics.ListAPIView):
    """Post question"""
    serializer_class = QuestionSerializer
    queryset = Quenstions.objects.all()

    pagination_class = SmallNopage

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostAnswer(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AnswerFilterByUser(generics.ListAPIView):
    """All ansewers by specific user"""
    serializer_class = AnswerSerializer
    queryset = Answers.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('user__id',)



import django_filters
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from questionnaire.models import Questionnaire
from questionnaire.serializers import QuestionnaireSerializer


class QuestionnaireFilter(django_filters.FilterSet):

    class Meta:
        model = Questionnaire
        fields = ['user']


class QuestionnaireView(ModelViewSet):
    serializer_class = QuestionnaireSerializer
    filterset_class = QuestionnaireFilter
    permission_classes = []
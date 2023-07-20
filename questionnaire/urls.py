from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questionnaire.views import QuestionnaireView

router = DefaultRouter()

router.register('questionnaire', QuestionnaireView, basename='questionnaire')

urlpatterns = [
    path('', include(router.urls)),
]

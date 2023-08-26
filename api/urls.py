from rest_framework import routers
from .views import QuizViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet, basename='quiz')

urlpatterns = [
    path('', include(router.urls)),
]
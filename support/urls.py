from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DialogListCreateView,
    MessageCreateView,
    DialogDetailView,
    PromptListView,
    QuestionAnswerAPIView,
    LikePromptAPIView,
    DislikePromptAPIView
)

urlpatterns = [
    path('support/dialogs/', DialogListCreateView.as_view(), name='dialog-list-create'),
    path('support/dialogs/<str:pk>/', DialogDetailView.as_view(), name='dialog-detail'),
    path('support/messages/', MessageCreateView.as_view(), name='message-list-create'),
    path('support/prompts/', PromptListView.as_view(), name='prompts-list'),
    path('support/questions-answers/', QuestionAnswerAPIView.as_view(), name='questions-answers'),
    path('support/prompts/<int:prompt_id>/like/', LikePromptAPIView.as_view(), name='like_prompt_api'),
    path('support/prompts/<int:prompt_id>/dislike/', DislikePromptAPIView.as_view(), name='dislike_prompt_api'),
]

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Prompt, Dialog, Message, QuestionAnswer, Like, Dislike
from .serializers import (
    DialogSerializer,
    MessageSerializer,
    DialogDetailSerializer,
    PromptSerializer,
    QuestionAnswerSerializer,
    LikeSerializer,
    DislikeSerializer
    )
from rest_framework import generics
from support import utils
import re
from django.db import transaction
from rest_framework.views import APIView
import requests
from config.settings import TOKEN_TRANSFORMRS_API

from django.contrib.auth import get_user_model

User = get_user_model()

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
HEADERS = {"Authorization": f"Bearer {TOKEN_TRANSFORMRS_API}"}


class PromptListView(generics.ListAPIView):
    serializer_class = PromptSerializer
    queryset = Prompt.objects.all()


class DialogListCreateView(generics.ListCreateAPIView):
    serializer_class = DialogSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return []
        return Dialog.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        prompt_id = request.data.get('prompt')
        user = request.user

        if user.is_anonymous:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_403_FORBIDDEN)

        try:
            prompt = Prompt.objects.get(id=prompt_id)
        except Prompt.DoesNotExist:
            return Response({"error": "Prompt not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, prompt=prompt)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DialogDetailView(generics.RetrieveAPIView):
    serializer_class = DialogDetailSerializer
    queryset = Dialog.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        user = self.request.user
        id = self.kwargs.get("pk")
        if user.is_anonymous:
            return Response({"error": "Invalid input data"}, status=status.HTTP_400_BAD_REQUEST)
        return queryset.filter(id=id, user=user).first()


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    # @transaction.atomic
    def create(self, request, *args, **kwargs):
        user_id = request.user
        query = request.data.get('text')
        dialog_id = request.data.get('dialog')

        if user_id.is_anonymous:
            return Response({"error": "User is not authenticated"}, status=status.HTTP_403_FORBIDDEN)

        if not user_id or not query or not dialog_id:
            return Response({"error": "Invalid input data"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dialog = Dialog.objects.get(id=dialog_id, user_id=user_id)

            # Поиск соответствующего промта
            messages = dialog.messages.all()
            # print(len(messages))
            # print(messages)

            if len(messages) == 0:
                prompt = dialog.prompt.text
                # print(prompt)
            else:
                prompt = " | ".join([m.text for m in messages])
                prompt = dialog.prompt.text + " | " + prompt
                prompt = "Твои предидущие сообщения: " + prompt
                # print(prompt)
            # prompt = prompt[]
            # prompt = prompt.replace(" ", "").replace(".", "").replace("-", "")
            # prompt=prompt+prompt
            print(len(prompt))
            # Логика обработки запроса чат-ботом
            query = query + " Если вопрос не относится к теме документа, напиши: Перевожу на специалиста."
            response = utils.query_predict_nlp(query, prompt[:30000])
            query = query.replace(" Если вопрос не относится к теме документа, напиши: Перевожу на специалиста.", "")
            # response = get_bot_response(query, prompt)
            cleaned_response = re.sub(r'[\u4e00-\u9fff]', '', response)
            with transaction.atomic():
                # Создание сообщений
                # Message.objects.create(dialog=dialog, text=query, is_user_message=True)
                # Message.objects.create(dialog=dialog, text=cleaned_response, is_user_message=False)
                # Создание сообщений
                Message.objects.bulk_create([
                    Message(dialog=dialog, text=query, is_user_message=True),
                    Message(dialog=dialog, text=cleaned_response, is_user_message=False)
                ])

            messages = Message.objects.filter(dialog=dialog)
            serializer = self.get_serializer(messages, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Dialog.DoesNotExist:
            return Response({"error": "Dialog not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return Response({"error": f"Internal server error, {e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_bot_response(query, prompt):
    # Заглушка для логики чат-бота, использующая промт
    if prompt:
        return f"Это ответ на ваш вопрос на основе {prompt.title}: {query}"
    else:
        return "Извините, я не могу ответить на ваш вопрос в данный момент."


class QuestionAnswerAPIView(APIView):

    def post(self, request, *args, **kwargs):
        question = request.data.get('question', '')

        # Отправляем запрос к API Hugging Face
        response = self.query_to_huggingface(question)
        answers = response.get('answers', [])
        filtered_objects = []
        for a in answers:
            filtered_object = QuestionAnswer.objects.filter(question=a).first()
            filtered_objects.append(filtered_object)

        # Возвращаем только первые 5 наиболее релевантных ответов
        serializer = QuestionAnswerSerializer(filtered_objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def query_to_huggingface(self, question):
        result=[]
        questions = list(QuestionAnswer.objects.all().values_list('question', flat=True))[:8000]
        chunk_size = 4000
        for i in range(0, len(questions), chunk_size):
            chunk = questions[i:i + chunk_size]
            print(i)
            payload = {
                "inputs": {
                    "source_sentence": question,
                    "sentences": chunk  # Возможно, вам здесь нужно передать список предложений из вашей базы данных
                }
            }
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            # Находим максимальное значение в списке
            max_value = max(list(response.json()))
            # Находим индекс максимального значения
            max_index = list(response.json()).index(max_value)
            result.append(chunk[max_index])
        # print(result)
        d={
            "answers":result
            }

        return d


class LikePromptAPIView(APIView):
    def post(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, id=prompt_id)
        print(prompt)
        like = Like.objects.create(prompt=prompt)
        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DislikePromptAPIView(APIView):
    def post(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, id=prompt_id)
        dislike = Dislike.objects.create(prompt=prompt)
        serializer = DislikeSerializer(dislike)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

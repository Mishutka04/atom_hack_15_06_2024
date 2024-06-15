from django.db import models
# from users.models import User
from django.contrib.auth import get_user_model

User = get_user_model()



class Prompt(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название")
    text = models.TextField(
        verbose_name="Текст"
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Промт"
        verbose_name_plural = "Промты"
    
    def likes_count(self):
        return self.likes.count()

    def dislikes_count(self):
        return self.dislikes.count()


class Like(models.Model):
    prompt = models.ForeignKey(Prompt, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"

    def __str__(self):
        return f"Лайк для {self.prompt.title}"


class Dislike(models.Model):
    prompt = models.ForeignKey(Prompt, related_name='dislikes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Дизлайк"
        verbose_name_plural = "Дизлайки"

    def __str__(self):
        return f"Дизлайк для {self.prompt.title}"


class Dialog(models.Model):
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dialogs',
        verbose_name="Пользователь")
    prompt = models.ForeignKey(
        Prompt,
        on_delete=models.CASCADE,
        related_name='dialogs',
        verbose_name="Промт"
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
        )

    def __str__(self):
        return f"Диалог {self.id} пользователя {self.user.email} на тему {self.prompt.title}"

    class Meta:
        verbose_name = "Диалог"
        verbose_name_plural = "Диалоги"


class Message(models.Model):
    dialog = models.ForeignKey(
        Dialog,
        on_delete=models.CASCADE,
        related_name='messages',
        verbose_name="Диалог")
    text = models.TextField(
        verbose_name="Текст сообщения"
        )
    is_user_message = models.BooleanField(
        default=True, 
        verbose_name="Сообщение пользователя"
        )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время отправки"
        )

    def __str__(self):
        return f"Сообщение в диалоге {self.dialog.id} в {self.timestamp}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


from django.db import models

class QuestionAnswer(models.Model):
    question = models.TextField("Вопрос")
    answer = models.TextField("Ответ")

    class Meta:
        verbose_name = "Вопрос и Ответ"
        verbose_name_plural = "Вопросы и Ответы"

    def __str__(self):
        return f"Вопрос: {self.question[:50]}..."  # Отображение первых 50 символов вопроса


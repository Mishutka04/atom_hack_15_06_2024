from django.contrib import admin
from .models import Prompt, Dialog, Message, QuestionAnswer, Like, Dislike


@admin.register(Prompt)
class PromptAdmin(admin.ModelAdmin):
    list_display = ('title', 'likes_count', 'dislikes_count')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'created_at')

@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    list_display = ('prompt', 'created_at')

admin.site.register(Dialog)
admin.site.register(Message)
admin.site.register(QuestionAnswer)
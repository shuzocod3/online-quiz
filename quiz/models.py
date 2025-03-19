from django.db import models
from django.conf import settings

# Create your models here.

class Quiz(models.Model):
    media = models.ImageField(upload_to="quiz_media", blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Questions(models.Model):
    media = models.ImageField(upload_to="question_media", blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    content = models.TextField()

    def __str__(self):
        return self.content


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answers")
    content = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.content

class UserAnswer(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    id_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name="id_answer")
    id_quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    gamecode = models.CharField(max_length=16)
from django.contrib import admin
from quiz.models import Quiz, Questions, Answer, UserAnswer

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Questions)
admin.site.register(Answer)
admin.site.register(UserAnswer)